from pyhcl_fancy.blocks.real.real_block import RealBlock


class ResourceBlock(RealBlock):
    resource_name: str

    def __init__(self):
        super().__init__()
        self.resource_name = ""


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> None:
        pass