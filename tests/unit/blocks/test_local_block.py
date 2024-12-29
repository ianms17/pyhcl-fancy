from pyhcl_fancy.blocks.reference.local.local_block import LocalBlock


def test_local_block_init():
    block = LocalBlock()
    assert block.content == {}
    assert block.file_path == ""


def test_local_block_parse_content(basic_parsed_terraform):
    local_block_content = basic_parsed_terraform["locals"]
    local_block = LocalBlock()
    local_block.parse(local_block_content[0], "terraform")
    assert local_block.content == {
        "queue_name": "my-other-queue",
        "lambda_name": "my-other-lambda"
    }


def test_local_block_parse_file_path(basic_parsed_terraform):
    local_block_content = basic_parsed_terraform["locals"]
    local_block = LocalBlock()
    local_block.parse(local_block_content[0], "terraform")
    assert local_block.file_path == "terraform"