from pyhcl_fancy.blocks.terraform_block import TerraformBlock
from typing import Any


class VariableBlock(TerraformBlock):
    def __init__(self):
        """
        Initializes a new instance of the VariableBlock class.

        Attributes:
            variable_name (str): The name of the variable.
            description (str): The description of the variable.
            type (str): The type of the variable.
            default (Any): The default value of the variable.
            validation (dict): The validation rules for the variable.
        """
        super().__init__()
        self.variable_name: str = ""
        self.description: str = ""
        self.type: str = ""
        self.default: Any = None
        self.validation: dict = {}

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass
