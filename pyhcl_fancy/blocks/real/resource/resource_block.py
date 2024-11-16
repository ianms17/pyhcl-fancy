from pyhcl_fancy.blocks.real.real_block import RealBlock


class ResourceBlock(RealBlock):
    resource_name: str

    def __init__(self, resource_name: str, state_path: str, count: int, for_each: list, content: dict):
        pass


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> None:
        pass