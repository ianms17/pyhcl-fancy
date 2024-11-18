from pyhcl_fancy.blocks.real.real_block import RealBlock


class ModuleBlock(RealBlock):
    module_name: str
    module_source: str


    def __init__(self):
        super().__init__()
        self.module_name = ""
        self.module_source = ""


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> None:
        pass