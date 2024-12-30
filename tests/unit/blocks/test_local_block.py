from pyhcl_fancy.blocks.reference.local.local_block import LocalBlock


def test_local_block_init():
    block = LocalBlock()
    assert block.content == {}
    assert block.file_path == ""


def test_local_block_parse_content_single_entry(raw_terraform_block):
    local_block_content = raw_terraform_block("locals/simple_locals.tf", "locals")
    local_block = LocalBlock()
    local_block.parse(local_block_content, "terraform")
    assert local_block.content == {
        "queue_name": "my-other-queue"
    }


def test_local_block_parse_file_path_single_entry(raw_terraform_block):
    local_block_content = raw_terraform_block("locals/simple_locals.tf", "locals")
    local_block = LocalBlock()
    local_block.parse(local_block_content, "terraform")
    assert local_block.file_path == "terraform"


def test_local_block_parse_content_multi_entry(raw_terraform_block):
    local_block_content = raw_terraform_block("locals/multi_entry_locals.tf", "locals")
    local_block = LocalBlock()
    local_block.parse(local_block_content, "terraform")
    assert local_block.content == {
        "queue_name": "my-other-queue",
        "lambda_name": "my-other-lambda"
    }


def test_local_block_parse_content_multi_block(raw_terraform_block):
    local_block_content = raw_terraform_block("locals/multi_block_locals.tf", "locals")
    print(local_block_content)
    local_block = LocalBlock()
    local_block.parse(local_block_content, "terraform")
    assert local_block.content == {
        "queue_name": "my-other-queue",
        "lambda_name": "my-other-lambda"
    }