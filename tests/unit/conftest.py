import pytest
import hcl2

from pyhcl_fancy.collection_tree.node import Node
from pyhcl_fancy.collection_tree.tree import CollectionTree
from pyhcl_fancy.blocks.real.module.module_block import ModuleBlock
from pyhcl_fancy.parser.parser import FancyParser

    
#
# Block Test Fixtures
#
@pytest.fixture
def raw_terraform_block():
    def _terraform_block(file_path: str, block_type: str) -> dict:
        with open(f"tests/unit/sample_terraform/{file_path}", "r") as f:
            return hcl2.load(f)[block_type]
    return _terraform_block
    

@pytest.fixture
def sample_file_node() -> Node:
    return Node()


@pytest.fixture
def submodule_file_node() -> Node:
    node = Node()
    node.submodule_state_path = "module.test_module"
    return node


#
# Node Test Fixtures
#
@pytest.fixture
def parent_node() -> Node:
    return Node()


@pytest.fixture
def child_node() -> Node:
    return Node()


#
# Collection Tree Test Fixtures
#
@pytest.fixture
def empty_collection_tree() -> CollectionTree:
    return CollectionTree()


@pytest.fixture
def flat_collection_tree() -> CollectionTree:
    tree = CollectionTree()
    root_node = Node()
    root_node.is_directory = True
    root_node.relative_file_path = "terraform/"
    tree.add_root(root_node)

    for i in range(3):
        node = Node()
        node.relative_file_path = f"terraform/{i}.tf"
        tree.root.add_child(node)

    sub_directory_node = Node()
    sub_directory_node.is_directory = True
    sub_directory_node.relative_file_path = "terraform/module/"
    tree.root.add_child(sub_directory_node)

    return tree


@pytest.fixture
def multi_level_collection_tree() -> CollectionTree:
    tree = CollectionTree()
    root_node = Node()
    root_node.is_directory = True
    root_node.relative_file_path = "terraform/"
    root_node.submodule_state_path = ""
    tree.add_root(root_node)

    for i in range(3):
        node = Node()
        node.relative_file_path = f"terraform/{i}.tf"
        tree.root.add_child(node)

    skipped_node = Node()
    skipped_node.is_directory = True
    skipped_node.is_leaf = False
    skipped_node.relative_file_path = "terraform/skipped/"
    skipped_node.submodule_state_path = "module.skipped"
    tree.root.add_child(skipped_node)

    for i in range(3, 6):
        node = Node()
        node.relative_file_path = f"terraform/skipped/{i}.tf"
        skipped_node.add_child(node)

    sub_directory_node = Node()
    sub_directory_node.is_directory = True
    sub_directory_node.is_leaf = False
    sub_directory_node.relative_file_path = "terraform/module/"
    sub_directory_node.submodule_state_path = "module.test_module"
    tree.root.add_child(sub_directory_node)

    for i in range(6, 9):
        node = Node()
        node.relative_file_path = f"terraform/module/{i}.tf"
        sub_directory_node.add_child(node)

    return tree


#
# Parser Fixtures
#
#
@pytest.fixture
def flat_parser() -> FancyParser:
    parser = FancyParser("tests/unit/sample_terraform/parser_flat")
    parser._read_tf_files()
    return parser


@pytest.fixture
def multi_level_parser() -> FancyParser:
    parser = FancyParser("tests/unit/sample_terraform/parser_multi_level")
    parser._read_tf_files()
    return parser


#
# Example Blocks for Testing
#
@pytest.fixture
def sample_module_block():
    module_block = ModuleBlock()
    module_block.module_name = "test_module"
    return module_block