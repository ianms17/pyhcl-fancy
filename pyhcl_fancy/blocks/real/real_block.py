from pyhcl_fancy.blocks.terraform_block import Block

class RealBlock(Block):
    state_path: str
    count: int
    for_each: list | dict
    content: dict

    
    def __init__(self, state_path: str, count: int, for_each: list | dict, content: dict):
        pass