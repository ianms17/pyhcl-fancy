from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class OutputBlock(TerraformBlock):
    variable_name: str
    description: str
    type: str
    default: any
    validation: dict

    def __init__(self):
        super().__init__()
        self.variable_name = ""
        self.description = ""
        self.type = ""
        self.default = None
        self.validation = {}

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass