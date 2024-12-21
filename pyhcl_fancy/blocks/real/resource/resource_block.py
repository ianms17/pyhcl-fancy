from pyhcl_fancy.blocks.real.real_block import RealBlock
from pyhcl_fancy.collection_tree.node import Node


class ResourceBlock(RealBlock):
    def __init__(self):
        """
        Initializes a new instance of the ResourceBlock class.

        Attributes:
            resource_type (str): The type of the resource.
            resource_name (str): The name of the resource.
        """
        super().__init__()
        self.resource_type: str = ""
        self.resource_name: str = ""

    def convert_to_hcl(self) -> str:
        pass

    def parse(
        self, raw_resource_dict: dict, resource_file_path: str, file_node: Node
    ) -> None:
        """
        Parses the raw_resource_dict to set the ResourceBlock's fields.

        Args:
            raw_resource_dict (dict): The raw dictionary from the terraform file for the resource block.
            resource_file_path (str): The path of the file where the resource block is defined.
            file_node (Node): The node representing the file in the collection tree.

        Returns:
            None
        """

        self.resource_type = raw_resource_dict.keys()[0]
        self.resource_name = raw_resource_dict[self.resource_type].keys()[0]
        if file_node.submodule_state_path is None:
            self.state_path = f"{self.resource_type}.{self.resource_name}"
        else:
            self.state_path = f"{file_node.submodule_state_path}.{self.resource_type}.{self.resource_name}"
        self.file_path = resource_file_path
        for attribute in raw_resource_dict[self.resource_type][self.resource_name]:
            self.content[attribute] = raw_resource_dict[self.resource_type][
                self.resource_name
            ][attribute]
