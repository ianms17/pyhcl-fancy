from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class OutputBlock(TerraformBlock):
    value: any
    description: str

    def __init__(self):
        super().__init__()
        self.value = None
        self.description = ""

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass