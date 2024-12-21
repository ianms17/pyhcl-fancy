from pyhcl_fancy.blocks.real.real_block import RealBlock
from pyhcl_fancy.collection_tree.node import Node


class ModuleBlock(RealBlock):
    def __init__(self):
        """
        Initializes a new instance of the ModuleBlock class.

        Attributes:
            module_name (str): The name of the module.
            module_source (str): The source of the module.
        """
        super().__init__()
        self.module_name: str = ""
        self.module_source: str = ""
        self.module_version: str = ""

    def convert_to_hcl(self) -> str:
        pass

    def parse(self, raw_module_dict: dict, module_file_path: str, parent_file_node: Node) -> None:
        self.module_name = raw_module_dict.keys()[0]
        self.file_path = module_file_path
        if parent_file_node.submodule_state_path == None:
            self.state_path = f"module.{self.module_name}"
        else:
            self.state_path = parent_file_node.submodule_state_path
        for attribute in raw_module_dict[self.module_name]:
            match attribute:
                case "source":
                    self.module_source = raw_module_dict[self.module_name][attribute]
                case "version":
                    self.module_version = raw_module_dict[self.module_name][attribute]
                case _:
                    self.content[attribute] = raw_module_dict[self.module_name][attribute]
