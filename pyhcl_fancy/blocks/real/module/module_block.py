from pyhcl_fancy.blocks.real.real_block import RealBlock


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

    def parse(self, module_name: str, module_file_path: str, module_content: dict) -> None:
        self.module_name = module_name
        self.file_path = module_file_path
        for attribute in module_content:
            match attribute:
                case "source":
                    self.module_source = module_content[attribute]
                case "version":
                    self.module_version = module_content[attribute]
                case _:
                    self.content[attribute] = module_content[attribute]
