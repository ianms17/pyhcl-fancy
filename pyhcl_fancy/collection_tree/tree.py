from pyhcl_fancy.collection_tree.node import Node


class CollectionTree:
    def __init__(self):
        self.root: Node = None
        self.height: int = 0
        self.is_flat: bool = False

    
    def add_root(self, node: Node) -> Node:
        if self.root is None:
            self.root = node
        return self.root
    

    def _increment_height(self):
        self.height += 1

    
    def _set_is_flat(self):
        return self.height == 1
        
