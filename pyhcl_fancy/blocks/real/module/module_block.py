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

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass
