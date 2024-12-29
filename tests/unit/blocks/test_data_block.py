from pyhcl_fancy.blocks.real.data.data_block import DataBlock


def test_data_block_init():
    block = DataBlock()
    assert block.data_name == ""
    assert block.data_type == ""
    assert block.file_path == ""
    assert block.state_path == ""
    assert block.content == {}
    assert block.for_each is None
    assert block.count is None


def test_basic_data_block_parse_data_name(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.data_name == "queue"


def test_basic_data_block_parse_data_type(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.data_type == "aws_sqs_queue"


def test_basic_data_block_parse_state_path(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.state_path == "data.aws_sqs_queue.queue"


def test_basic_data_block_parse_content(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.content["name"] == "my-queue"


def test_basic_data_block_parse_for_each(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.for_each is None


def test_basic_data_block_parse_count(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.count == 0


def test_basic_data_block_parse_file_path(basic_parsed_terraform, sample_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", sample_file_node)
    assert data_block.file_path == "terraform"


def test_submodule_data_block_parse_state_path(basic_parsed_terraform, submodule_file_node):
    data_block_list = basic_parsed_terraform["data"]
    data_block = DataBlock()
    data_block.parse(data_block_list[0], "terraform", submodule_file_node)
    assert data_block.state_path == "module.test_module.data.aws_sqs_queue.queue"