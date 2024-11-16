from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class ProviderBlock(TerraformBlock):
    type: str
    region: str
    alias: str
    assume_role: str
    default_tags: dict

    def __init__(self, file_path: str, resource_type: str, type: str, region: str, alias: str, assume_role: str, default_tags: dict):
        pass

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass