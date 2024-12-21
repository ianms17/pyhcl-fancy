from pyhcl_fancy.blocks.terraform_block import TerraformBlock


class LocalBlock(TerraformBlock):
    def __init__(self):
        """
        Initializes a new instance of the LocalBlock class.

        Attributes:
            content (dict): The content of the locals block.
        """
        super().__init__()
        self.content: dict = {}

    def convert_to_hcl(self) -> str:
        pass

    def parse(self, raw_locals_dict: dict, locals_file_path: str) -> str:
        """
        Parses the raw locals dictionary and sets the content of the LocalBlock.

        Args:
            raw_locals_dict (dict): The raw locals dictionary to parse.
            locals_file_path (str): The path of the file containing the locals block.

        Returns:
            str: The parsed content of the locals block.
        """
        self.file_path = locals_file_path
        self.content = raw_locals_dict
