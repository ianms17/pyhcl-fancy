from pyhcl_fancy.blocks.reference.output.output_block import OutputBlock


def test_output_block_init():
    block = OutputBlock()
    assert block.name == ""
    assert block.value == None
    assert block.description == ""
    assert block.options == {}
    assert block.file_path == ""


def test_output_block_parse_name(basic_parsed_terraform):
    output_block_content = basic_parsed_terraform["output"]
    output_block = OutputBlock()
    output_block.parse(output_block_content[0], "terraform")
    assert output_block.name == "key_arn"


def test_output_block_parse_value(basic_parsed_terraform):
    output_block_content = basic_parsed_terraform["output"]
    output_block = OutputBlock()
    output_block.parse(output_block_content[0], "terraform")
    assert output_block.value == "${aws_kms_key.key.arn}"


def test_output_block_parse_description(basic_parsed_terraform):
    output_block_content = basic_parsed_terraform["output"]
    output_block = OutputBlock()
    output_block.parse(output_block_content[0], "terraform")
    assert output_block.description == "ARN of the KMS key"


def test_output_block_parse_options(basic_parsed_terraform):
    output_block_content = basic_parsed_terraform["output"]
    output_block = OutputBlock()
    output_block.parse(output_block_content[0], "terraform")
    assert output_block.options == {
        "sensitive": False
    }

def test_output_block_parse_file_path(basic_parsed_terraform):
    output_block_content = basic_parsed_terraform["output"]
    output_block = OutputBlock()
    output_block.parse(output_block_content[0], "terraform")
    assert output_block.file_path == "terraform"