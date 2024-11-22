from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class LocalBlock(TerraformBlock):
    def __init__(self):
        """
        Initializes a new instance of the LocalBlock class.

        Attributes:
            content (dict): The content of the locals block.
        """
        super().__init__()
        self.content: dict = {}


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> str:
        pass