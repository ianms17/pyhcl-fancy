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
        """
        Parses the raw meta dictionary and updates the TerraformMetaBlock attributes.

        This function iterates over the settings in the raw meta dictionary and
        updates the corresponding attributes of the TerraformMetaBlock based on
        the setting type. It handles backend configurations by setting the backend
        type and configuration, and also processes required providers. Any other
        settings are stored in the options dictionary.

        Args:
            raw_meta_dict (dict): The dictionary containing raw meta settings.
            meta_file_path (str): The path to the file containing meta configuration.

        Returns:
            None
        """

        for setting in raw_meta_dict:
            match setting:
                case "backend":
                    self.backend_type = raw_meta_dict[setting].keys()[0]
                    self.backend_config = raw_meta_dict[setting][self.backend_type]
                case "required_providers":
                    self.required_providers = raw_meta_dict[setting]
                case _:
                    self.options[setting] = raw_meta_dict[setting]
