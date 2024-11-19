from pyhcl_fancy.collection_tree import CollectionTree, Node

from pyhcl_fancy.parser.utils import (
    _open_all_tf_files
)


class FancyParser: 
    def __init__(self, terraform_directory: str):
        self.terraform_directory = terraform_directory
        self.terraform_content: dict = {}
        self.collection_tree: CollectionTree = CollectionTree()

    
    def read_tf_files(self) -> None:
        self.terraform_content = _open_all_tf_files(self.terraform_directory)