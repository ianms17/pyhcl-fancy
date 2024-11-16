from pyhcl_fancy.blocks.real.real_block import RealBlock


class ModuleBlock(RealBlock):
    module_name: str
    module_source: str


    def __init__(self, module_name: str, module_source: str, state_path: str, count: int, for_each: list, content: dict):
        pass


    def convert_to_hcl(self) -> str:
        pass


    def read_in(self) -> None:
        pass