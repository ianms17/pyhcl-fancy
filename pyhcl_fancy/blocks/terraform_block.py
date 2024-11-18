class TerraformBlock:
    file_path: str
    resource_type: str

    def __init__(self):
        self.file_path = ""
        self.resource_type = ""


    def _get_resource_type(self) -> str:
        return ""
    

    def _get_file_path(self) -> str:
        return ""
    

    def reverse_engineer_variables(self) -> None:
        return None