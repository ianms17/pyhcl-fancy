from pyhcl_fancy.collection_tree.node import Node
from pyhcl_fancy.parser.parser import FancyParser
from pyhcl_fancy.blocks.real.module.module_block import ModuleBlock
from pyhcl_fancy.collection_tree.exceptions import (
    FileNodeNotFoundError,
    DirectoryNodeNotFoundError,
    InvalidMoveLocationError
) 


class CollectionTree:
    def __init__(self):
        """
        Initializes a new instance of the CollectionTree class.

        Attributes:
            root (Node): The root node of the collection tree.
            height (int): The height of the collection tree.
            is_flat (bool): A flag indicating whether the tree is flat.
        """
        self.root: Node = None
        self.height: int = 0
        self.is_flat: bool = False

    def add_root(self, node: Node) -> Node:
        """
        Adds a root node to the collection tree if one does not already exist.

        Args:
            node: The root node to add to the collection tree.

        Returns:
            The root node of the collection tree.
        """
        if self.root is None:
            self.root = node
        return self.root


    def add_node_to_directory(self, directory: str, child: Node) -> Node:
        """
        Adds a child node to a specified directory node within the collection tree.

        Args:
            directory (str): The path of the directory where the child node will be added.
            child (Node): The child node to add to the specified directory.

        Returns:
            Node: The directory node to which the child was added.
        """
        directory_node = self.find_directory_node(self.root, directory)
        return directory_node.add_child(child)

    def add_submodule_directory(self, directory_node: Node, file_path: str) -> Node:
        """
        Adds a submodule directory to the collection tree under a specific file node.

        Args:
            directory_node (Node): The node of the directory to be added as a submodule.
            file_path (str): The path of the file node under which the submodule is to be added.

        Returns:
            Node: The file node under which the submodule is added.
        """
        file_node = self.find_file_node(directory_node, file_path)
        return file_node.add_child(directory_node)

    def find_directory_node(self, node: Node, directory: str) -> Node:
        """
        Recursively searches for a directory node within the collection tree
        given a directory path.

        Args:
            node (Node): The current node to search in the collection tree.
            directory (str): The path of the directory to search for.

        Returns:
            Node: The directory node if found, otherwise None.
        """
        for child in node.children:
            if child.is_directory and child.relative_file_path == directory:
                return child
            else:
                if child.is_leaf:
                    continue
                return self.find_directory_node(child, directory)
        
        raise DirectoryNodeNotFoundError(f"The directory {directory} was not found in the collection tree.")

    def find_file_node(self, node: Node, file_path: str) -> Node:
        """
        Recursively searches for a file node within the collection tree
        given a file path.

        Args:
            node (Node): The current node to search in the collection tree.
            file_path (str): The path of the file to search for.

        Returns:
            Node: The file node if found, otherwise None.
        """
        for child in node.children:
            if child.relative_file_path == file_path:
                return child
            else:
                if child.is_leaf:
                    continue
                return self.find_file_node(child, file_path)
            
        raise FileNodeNotFoundError(f"The file {file_path} was not found in the collection tree.")
    

    def move_node(self, source: Node, destination: Node, caller: ModuleBlock) -> Node:
        if source == destination:
            raise InvalidMoveLocationError("Cannot move a node to itself.")
        elif source.parent == destination:
            raise InvalidMoveLocationError("The destination node is already the parent of the source node.")
        elif source.is_directory == destination.is_directory:
            raise InvalidMoveLocationError(
                f"The source and destination nodes must not have the same directory status. Both nodes have directory status {source.is_directory}."
            )
        
        curr_parent = source.parent
        for child in curr_parent.children:
            if child == source:
                curr_parent.children.remove(child)
                destination.add_child(source)
                if curr_parent.submodule_state_path == "":
                    destination.submodule_state_path = f"module.{caller.module_name}"
                else:
                    destination.submodule_state_path = f"{curr_parent.submodule_state_path}.module.{caller.module_name}"

    def _increment_height(self) -> None:
        self.height += 1

    def _set_is_flat(self) -> None:
        self.is_flat = self.height == 1
