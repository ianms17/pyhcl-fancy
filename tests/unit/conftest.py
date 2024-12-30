import pytest
import hcl2

from pyhcl_fancy.collection_tree.node import Node


@pytest.fixture
def basic_parsed_terraform() -> dict:
    with open("tests/unit/sample_terraform/basic/main.tf", "r") as f:
        return hcl2.load(f)
    

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