from pyhcl_fancy.parser.utils import (
    _open_all_tf_files
)


class FancyParser:
    terraform_directory: str
    terraform_content: dict

    
    def __init__(self, terraform_directory: str):
        self.terraform_directory = terraform_directory

    
    def read_tf_files(self) -> None:
        self.terraform_content = _open_all_tf_files(self.terraform_directory)