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
    found_node = flat_collection_tree.find_directory_node("terraform/")
    assert found_node == flat_collection_tree.root


def test_collection_tree_find_directory_node_at_leaf(flat_collection_tree):
    found_node = flat_collection_tree.find_directory_node("terraform/module/")
    assert found_node.is_leaf and found_node.relative_file_path == "terraform/module/"


def test_collection_tree_find_directory_node_skipped_leaf(multi_level_collection_tree):
    found_node = multi_level_collection_tree.find_directory_node("terraform/module/")
    print(found_node)
    assert found_node.relative_file_path == "terraform/module/"


def test_collection_tree_find_directory_node_not_found(flat_collection_tree):
    with pytest.raises(DirectoryNodeNotFoundError):
        flat_collection_tree.find_directory_node("terraform/invalid/")


#
# Find File Node Tests
#
def test_collection_tree_find_file_node_at_root_level(flat_collection_tree):
    found_node = flat_collection_tree.find_file_node("terraform/0.tf")
    assert found_node.relative_file_path == "terraform/0.tf"


def test_collection_tree_find_file_node_at_nested_level(multi_level_collection_tree):
    found_node = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    assert found_node.relative_file_path == "terraform/module/6.tf"


def test_collection_tree_find_file_node_not_found_flat(flat_collection_tree):
    with pytest.raises(FileNodeNotFoundError):
        flat_collection_tree.find_file_node("terraform/invalid.tf")


def test_collection_tree_find_file_node_not_found_multi_level(
    multi_level_collection_tree,
):
    with pytest.raises(FileNodeNotFoundError):
        multi_level_collection_tree.find_file_node("terraform/invalid.tf")


#
# Move Node Tests
#
def test_collection_tree_move_node_source_removed_from_parent(
    multi_level_collection_tree, sample_module_block
):
    source = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node("terraform/")
    source_parent = source.parent
    moved_node = multi_level_collection_tree.move_node(
        source, destination, sample_module_block
    )
    assert moved_node not in source_parent.children


def test_collection_tree_move_node_source_added_to_destination(
    multi_level_collection_tree, sample_module_block
):
    source = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node("terraform/")
    moved_node = multi_level_collection_tree.move_node(
        source, destination, sample_module_block
    )

    # moved node and source are the same, validate both
    assert moved_node in destination.children
    assert source in destination.children


def test_collection_tree_move_node_source_destination_not_has_state_path(
    multi_level_collection_tree, sample_module_block
):
    source = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node("terraform/")
    moved_node = multi_level_collection_tree.move_node(
        source, destination, sample_module_block
    )
    assert moved_node.submodule_state_path == "module.test_module"


def test_collection_tree_move_node_destination_has_state_path(
    multi_level_collection_tree, sample_module_block
):
    source = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node("terraform/skipped/")
    moved_node = multi_level_collection_tree.move_node(
        source, destination, sample_module_block
    )
    assert moved_node.submodule_state_path == "module.skipped.module.test_module"


def test_collection_tree_move_node_move_file_to_directory(
    multi_level_collection_tree, sample_module_block
):
    source = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    destination = multi_level_collection_tree.find_directory_node("terraform/")
    multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert source in destination.children


def test_collection_tree_move_node_move_directory_to_file(
    multi_level_collection_tree, sample_module_block
):
    destination = multi_level_collection_tree.find_file_node("terraform/module/6.tf")
    source = multi_level_collection_tree.find_directory_node("terraform/skipped/")
    multi_level_collection_tree.move_node(source, destination, sample_module_block)
    assert source in destination.children


def test_collection_tree_move_node_source_and_destination_same(
    multi_level_collection_tree, sample_module_block
):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_directory_node(
            "terraform/module/"
        )
        source = multi_level_collection_tree.find_directory_node("terraform/module/")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)


def test_collection_tree_move_node_node_already_in_destination(
    multi_level_collection_tree, sample_module_block
):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_directory_node("terraform/")
        source = multi_level_collection_tree.find_file_node("terraform/0.tf")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)


def test_collection_tree_move_node_source_and_destination_both_directories(
    multi_level_collection_tree, sample_module_block
):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_directory_node(
            "terraform/module/"
        )
        source = multi_level_collection_tree.find_directory_node("terraform/skipped/")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)


def test_collection_tree_move_node_source_and_destination_both_files(
    multi_level_collection_tree, sample_module_block
):
    with pytest.raises(InvalidMoveLocationError):
        destination = multi_level_collection_tree.find_file_node("terraform/0.tf")
        source = multi_level_collection_tree.find_file_node("terraform/1.tf")
        multi_level_collection_tree.move_node(source, destination, sample_module_block)


#
# Visualize Tests
#
def test_collection_tree_visualize_flat(flat_parser, capsys):
    flat_parser.parse()
    flat_parser.collection_tree.visualize()

    expected_output = """tests/unit/sample_terraform/parser_flat
|  tests/unit/sample_terraform/parser_flat/data.tf
|  tests/unit/sample_terraform/parser_flat/outputs.tf
|  tests/unit/sample_terraform/parser_flat/locals.tf
|  tests/unit/sample_terraform/parser_flat/kms.tf
|  tests/unit/sample_terraform/parser_flat/variables.tf
|  tests/unit/sample_terraform/parser_flat/lambda.tf
|  tests/unit/sample_terraform/parser_flat/provider.tf
|  tests/unit/sample_terraform/parser_flat/sqs.tf
|  tests/unit/sample_terraform/parser_flat/terraform.tf
"""

    output = capsys.readouterr().out
    for line in expected_output.split("\n"):
        assert line in output


def test_collection_tree_visualize_multi_level(multi_level_parser, capsys):
    multi_level_parser.parse()
    multi_level_parser.collection_tree.visualize()

    expected_output = """tests/unit/sample_terraform/parser_multi_level
|  tests/unit/sample_terraform/parser_multi_level/data.tf
|  tests/unit/sample_terraform/parser_multi_level/outputs.tf
|  tests/unit/sample_terraform/parser_multi_level/locals.tf
|  tests/unit/sample_terraform/parser_multi_level/kms.tf
|  tests/unit/sample_terraform/parser_multi_level/variables.tf
|  tests/unit/sample_terraform/parser_multi_level/lambda.tf
|  |  tests/unit/sample_terraform/parser_multi_level/lambda
|  |  |  tests/unit/sample_terraform/parser_multi_level/lambda/outputs.tf
|  |  |  tests/unit/sample_terraform/parser_multi_level/lambda/main.tf
|  |  |  tests/unit/sample_terraform/parser_multi_level/lambda/variables.tf
|  tests/unit/sample_terraform/parser_multi_level/provider.tf
|  tests/unit/sample_terraform/parser_multi_level/sqs.tf
|  tests/unit/sample_terraform/parser_multi_level/terraform.tf
"""

    output = capsys.readouterr().out
    for line in expected_output.split("\n"):
        assert line in output


def test_collection_tree_visualize_multi_nested(multi_nested_parser, capsys):
    multi_nested_parser.parse()
    multi_nested_parser.collection_tree.visualize()

    expected_output = """tests/unit/sample_terraform/parser_multi_nested
|  tests/unit/sample_terraform/parser_multi_nested/main.tf
|  |  tests/unit/sample_terraform/parser_multi_nested/modules/lambda
|  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/lambda/main.tf
|  |  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/sqs
|  |  |  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/sqs/main.tf
|  |  |  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/sqs/variables.tf
|  |  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/sns
|  |  |  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/sns/main.tf
|  |  |  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/sns/variables.tf
|  |  |  tests/unit/sample_terraform/parser_multi_nested/modules/lambda/variables.tf
|  tests/unit/sample_terraform/parser_multi_nested/provider.tf
"""

    output = capsys.readouterr().out
    for line in expected_output.split("\n"):
        assert line in output
