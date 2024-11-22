class TerraformBlock:
    def __init__(self):
        """
        Initializes a new instance of the TerraformBlock class.

        Attributes:
            file_path (str): The path of the file where the block is defined
        """
        self.file_path: str = ""

    def _get_resource_type(self) -> str:
        return ""

    def _get_file_path(self) -> str:
        return ""

    def reverse_engineer_variables(self) -> None:
        return None
