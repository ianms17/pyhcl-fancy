from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class OutputBlock(TerraformBlock):
    variable_name: str
    description: str
    type: str
    default: any
    validation: dict

    def __init__(self, file_path: str, resource_type: str, variable_name: str, description: str, type: str, default: any, validation: dict):
        pass

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass