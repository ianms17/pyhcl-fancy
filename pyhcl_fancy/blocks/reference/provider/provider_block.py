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
        self.options: dict = {}

    def convert_to_hcl(self) -> str:
        pass

    def parse(self, raw_provider_dict: dict, provider_file_path: str) -> None:
        self.type = raw_provider_dict.keys()[0]
        self.file_path = provider_file_path
        for attribute in raw_provider_dict[self.type]:
            match attribute:
                case "region":
                    self.region = raw_provider_dict[self.type][attribute]
                case "alias":
                    self.alias = raw_provider_dict[self.type][attribute]
                case "assume_role":
                    self.assume_role = raw_provider_dict[self.type][attribute]
                case "default_tags":
                    self.default_tags = raw_provider_dict[self.type][attribute]
                case _:
                    self.options[attribute] = raw_provider_dict[self.type][attribute]
