from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class OutputBlock(TerraformBlock):
    value: any
    description: str

    def __init__(self, file_path: str, resource_type: str, value: any, description: str):
        pass

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass