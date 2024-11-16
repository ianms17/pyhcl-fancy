from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class LocalBlock(TerraformBlock):
    content: dict


    def __init__(self, file_path: str, resource_type: str, content: dict):
        pass


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> str:
        pass