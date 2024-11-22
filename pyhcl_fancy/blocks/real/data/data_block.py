from pyhcl_fancy.blocks.real.real_block import RealBlock


class DataBlock(RealBlock):   
    def __init__(self):
        """
        Initializes a new instance of the DataBlock class.

        Attributes:
            data_type (str): The type of the data block.
            data_name (str): The name of the data block.
        """
        super().__init__()
        self.data_type: str = ""
        self.data_name: str = ""


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> None:
        pass