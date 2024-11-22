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
        self.backend: dict = {}
        self.required_providers: list = []

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> str:
        pass
