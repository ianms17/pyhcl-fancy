from pyhcl_fancy.blocks.terraform_block import TerraformBlock
from typing import Any


class OutputBlock(TerraformBlock):
    def __init__(self):
        """
        Initializes a new instance of the OutputBlock class.

        Attributes:
            value (Any): The value of the output variable.
            description (str): The description of the output variable.
        """
        super().__init__()
        self.value: Any = None
        self.description: str = ""

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass