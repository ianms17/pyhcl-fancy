from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class ProviderBlock(TerraformBlock):
    def __init__(self):
        """
        Initializes a new instance of the ProviderBlock class.

        Attributes:
            type (str): The type of the provider.
            region (str): The region for the provider.
            alias (str): The alias of the provider.
            assume_role (str): The assume role for the provider.
            default_tags (dict): The default tags for the provider.
        """
        super().__init__()
        self.type: str = ""
        self.region: str = ""
        self.alias: str = ""
        self.assume_role: str = ""
        self.default_tags: dict = {}

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass
