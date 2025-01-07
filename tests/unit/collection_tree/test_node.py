from pyhcl_fancy.collection_tree.node import Node


def test_node_init():
    node = Node()
    assert node.blocks == []
    assert node.is_directory is False
    assert node.relative_file_path == ""
    assert node.parent is None
    assert node.children == []
    assert node.is_root is False
    assert node.is_leaf is True


def test_node_add_child_parent_has_child(parent_node, child_node):
    parent_node.add_child(child_node)
    assert parent_node.children == [child_node]


def test_node_add_child_child_has_parent(parent_node, child_node):
    parent_node.add_child(child_node)
    assert child_node.parent == parent_node


def test_node_add_child_parent_is_not_leaf(parent_node, child_node):
    parent_node.add_child(child_node)
    assert parent_node.is_leaf is False