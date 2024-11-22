from pyhcl_fancy.blocks.real.real_block import RealBlock


class ResourceBlock(RealBlock):
    def __init__(self):
        """
        Initializes a new instance of the ResourceBlock class.

        Attributes:
            resource_type (str): The type of the resource.
            resource_name (str): The name of the resource.
        """
        super().__init__()
        self.resource_type: str = ""
        self.resource_name: str = ""

    def convert_to_hcl(self) -> str:
        pass

    def read_in(self) -> None:
        pass
