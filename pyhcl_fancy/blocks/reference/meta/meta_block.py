from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class TerraformMetaBlock(TerraformBlock):
    def __init__(self):
        """
        Initializes a new instance of the TerraformMetaBlock class.

        Attributes:
            backend (dict): The backend configuration for Terraform.
            required_providers (list): A list of required providers for the Terraform configuration.
        """
        super().__init__()
        self.backend_type: str = ""
        self.backend_config: dict = {}
        self.required_providers: dict = {}
        self.options: dict = {}

    def convert_to_hcl(self) -> str:
        pass

    def parse(self, raw_meta_dict: dict, meta_file_path: str) -> str:
        for setting in raw_meta_dict:
            match setting:
                case "backend":
                    self.backend_type = raw_meta_dict[setting].keys()[0]
                    self.backend_config = raw_meta_dict[setting][self.backend_type]
                case "required_providers":
                    self.required_providers = raw_meta_dict[setting]
                case _:
                    self.options[setting] = raw_meta_dict[setting]
