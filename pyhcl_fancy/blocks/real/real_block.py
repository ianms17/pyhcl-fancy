from pyhcl_fancy.blocks.terraform_block import Block

class RealBlock(Block):
    def __init__(self):
        """
        Initializes a new instance of the RealBlock class.

        Attributes:
            state_path (str): The state path of the block.
            count (int): The count of the block.
            for_each (list | dict): The for_each of the block.
            content (dict): The content of the block.
        """
        super().__init__()
        self.state_path: str = ""
        self.count: int = 0
        self.for_each: list | dict = None
        self.content: dict = {}