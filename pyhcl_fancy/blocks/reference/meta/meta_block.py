from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class TerraformMetaBlock(TerraformBlock):
    backend: dict
    required_providers: list

    def __init__(self):
        super().__init__()
        self.backend = {}
        self.required_providers = []


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> str:
        pass