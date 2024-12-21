from pyhcl_fancy.blocks.real.real_block import RealBlock


def test_real_block_init():
    real_block = RealBlock()
    assert real_block.state_path == ""
    assert real_block.count == 0
    assert real_block.for_each is None
    assert real_block.content == {}
    assert real_block.file_path == ""