from typing import Self
from pyhcl_fancy.collection_tree.utils import (
    _is_directory
)


class Node:
    def __init__(self):
        self.is_directory: bool = False
        self.relative_file_path: str = ""
        self.parent: Node = None
        self.children: list[Node] = []
        self.is_root: bool = False
        self.is_leaf: bool = True
        
    def set_is_directory(self, file_path: str) -> None:
        self.is_directory = _is_directory(file_path) 

    
    def add_child(self, child: Self) -> None:
        self.children.append(child)