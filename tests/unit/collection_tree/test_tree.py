import pytest

from pyhcl_fancy.collection_tree.tree import CollectionTree
from pyhcl_fancy.collection_tree.exceptions import (
    FileNodeNotFoundError,
    DirectoryNodeNotFoundError,
    InvalidMoveLocationError,
)


def test_collection_tree_init():
    tree = CollectionTree()
    assert tree.root is None


#
# Add Root Tests
#
def test_collection_tree_add_root_root_set(empty_collection_tree, child_node):
    empty_collection_tree.add_root(child_node)
    assert empty_collection_tree.root == child_node


def test_collection_tree_add_root_root_returned(empty_collection_tree, child_node):
    assert empty_collection_tree.add_root(child_node) == child_node


#
# Find Directory Node Tests
#
def test_collection_tree_find_directory_node_at_root(flat_collection_tree):
    found_node = flat_collection_tree.find_directory_node(flat_collection_tree.root, "terraform/")
    assert found_node == flat_collection_tree.root


def test_collection_tree_find_directory_node_at_leaf(flat_collection_tree):
    found_node = flat_collection_tree.find_directory_node(flat_collection_tree.root, "terraform/module/")
    assert found_node.is_leaf == True and found_node.relative_file_path == "terraform/module/"


def test_collection_tree_find_directory_node_skipped_leaf(multi_level_collection_tree):
    found_node = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/module/")
    print(found_node)
    assert found_node.relative_file_path == "terraform/module/"


def test_collection_tree_find_directory_node_not_found(flat_collection_tree):
    found_node = flat_collection_tree.find_directory_node(flat_collection_tree.root, "terraform/invalid/")
    assert found_node is None

#
# Find File Node Tests
#
def test_collection_tree_find_file_node_at_root_level(flat_collection_tree):
    found_node = flat_collection_tree.find_file_node(flat_collection_tree.root, "terraform/0.tf")
    assert found_node.relative_file_path == "terraform/0.tf"


def test_collection_tree_find_file_node_at_nested_level(multi_level_collection_tree):
    found_node = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    assert found_node.relative_file_path == "terraform/module/6.tf"


def test_collection_tree_find_file_node_not_found_flat(flat_collection_tree):
    found_node = flat_collection_tree.find_file_node(flat_collection_tree.root, "terraform/invalid.tf")
    assert found_node is None


def test_collection_tree_find_file_node_not_found_multi_level(multi_level_collection_tree):
    found_node = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/invalid.tf")
    assert found_node is None


#
# Move Node Tests
#
def test_collection_tree_move_node_source_removed_from_parent(multi_level_collection_tree, sample_module_block):
    source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/")
    source_parent = source.parent
    moved_node = multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert moved_node not in source_parent.children


def test_collection_tree_move_node_source_added_to_destination(multi_level_collection_tree, sample_module_block):
    source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/")
    moved_node = multi_level_collection_tree.move_node(source, destination, sample_module_block)
    
    # moved node and source are the same, validate both
    assert moved_node in destination.children
    assert source in destination.children


def test_collection_tree_move_node_source_destination_not_has_state_path(multi_level_collection_tree, sample_module_block):
    source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/")
    moved_node = multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert moved_node.submodule_state_path == "module.test_module"


def test_collection_tree_move_node_destination_has_state_path(multi_level_collection_tree, sample_module_block):
    source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/skipped/")
    moved_node = multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert moved_node.submodule_state_path == "module.skipped.module.test_module"


def test_collection_tree_move_node_move_file_to_directory(multi_level_collection_tree, sample_module_block):
    source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/")
    multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert source in destination.children
    

def test_collection_tree_move_node_move_directory_to_file(multi_level_collection_tree, sample_module_block):
    destination = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/module/6.tf")
    source = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/skipped/")
    multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert source in destination.children
    


def test_collection_tree_move_node_source_and_destination_same(multi_level_collection_tree, sample_module_block):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/module/")
        source = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/module/")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)


def test_collection_tree_move_node_node_already_in_destination(multi_level_collection_tree, sample_module_block):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/")
        source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/0.tf")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)

def test_collection_tree_move_node_source_and_destination_both_directories(multi_level_collection_tree, sample_module_block):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/module/")
        source = multi_level_collection_tree.find_directory_node(multi_level_collection_tree.root, "terraform/skipped/")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)


def test_collection_tree_move_node_source_and_destination_both_files(multi_level_collection_tree, sample_module_block):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/0.tf")
        source = multi_level_collection_tree.find_file_node(multi_level_collection_tree.root, "terraform/1.tf")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)