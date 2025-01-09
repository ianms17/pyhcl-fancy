from pyhcl_fancy.blocks.real.resource.resource_block import ResourceBlock


def test_resource_block_init():
    block = ResourceBlock()
    assert block.resource_type == ""
    assert block.resource_name == ""
    assert block.content == {}
    assert block.state_path == ""
    assert block.for_each is None
    assert block.count is None
    assert block.file_path == ""


def test_simple_resource_block_parse_resource_type(
    raw_terraform_block, sample_file_node
):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.resource_type == "aws_sqs_queue"


def test_simple_resource_block_parse_resource_name(
    raw_terraform_block, sample_file_node
):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.resource_name == "queue"


def test_simple_resource_block_parse_resource_content(
    raw_terraform_block, sample_file_node
):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.content == {
        "name": "terraform-example-queue.fifo",
        "fifo_queue": True,
        "content_based_deduplication": True,
    }


def test_simple_resource_block_parse_resource_state_path(
    raw_terraform_block, sample_file_node
):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.state_path == "aws_sqs_queue.queue"


def test_simple_resource_block_parse_for_each(raw_terraform_block, sample_file_node):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.for_each is None


def test_simple_resource_block_parse_count(raw_terraform_block, sample_file_node):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.count is None


def test_simple_resource_block_parse_file_path(raw_terraform_block, sample_file_node):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", sample_file_node)
    assert resource_block.file_path == "terraform"


def test_simple_submodule_resource_block_parse_state_path(
    raw_terraform_block, submodule_file_node
):
    resource_block_content = raw_terraform_block(
        "resource/simple_resource.tf", "resource"
    )
    resource_block = ResourceBlock()
    resource_block.parse(resource_block_content[0], "terraform", submodule_file_node)
    assert resource_block.state_path == "module.test_module.aws_sqs_queue.queue"
