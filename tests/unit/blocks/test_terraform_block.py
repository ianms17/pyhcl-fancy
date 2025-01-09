from pyhcl_fancy.blocks.terraform_block import TerraformBlock


def test_terraform_block_init():
    block = TerraformBlock()
    assert block.file_path == ""
