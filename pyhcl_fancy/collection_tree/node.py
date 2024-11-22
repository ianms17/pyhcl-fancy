from typing import Self
from pyhcl_fancy.collection_tree.utils import (
    _is_directory
)


class Node:
    def __init__(self):
        """
        Initializes a new instance of the Node class.

        Attributes:
            is_directory (bool): True if the node is a directory, otherwise False.
            relative_file_path (str): The relative path of the file or directory represented by the node.
            parent (Node): The parent node in the collection tree.
            children (list[Node]): A list of child nodes in the collection tree.
            is_root (bool): True if the node is the root node of the collection tree, otherwise False.
            is_leaf (bool): True if the node is a leaf node in the collection tree, otherwise False.
        """
        self.is_directory: bool = False
        self.relative_file_path: str = ""
        self.parent: Node = None
        self.children: list[Node] = []
        self.is_root: bool = False
        self.is_leaf: bool = True
        
    def set_is_directory(self, file_path: str) -> None:
        """
        Sets whether the node is a directory or not, given the file path of the node.

        Args:
            file_path (str): The file path of the node.

        Returns:
            None
        """
        self.is_directory = _is_directory(file_path) 

    
    def add_child(self, child: Self) -> None:
        """
        Adds a child node to the current node's list of children.

        Args:
            child (Node): The child node to be added to this node's children list.

        Returns:
            None
        """
        self.children.append(child)