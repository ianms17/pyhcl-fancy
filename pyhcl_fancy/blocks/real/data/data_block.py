from pyhcl_fancy.blocks.real.real_block import RealBlock


class DataBlock(RealBlock):
    data_name: str
    
    def __init__(self):
        super().__init__()
        self.data_name = ""


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> None:
        pass