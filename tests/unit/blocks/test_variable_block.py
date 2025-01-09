from pyhcl_fancy.blocks.reference.variable.variable_block import VariableBlock


def test_variable_block_init():
    block = VariableBlock()
    assert block.variable_name == ""
    assert block.description == ""
    assert block.type == ""
    assert block.default is None
    assert block.validation == {}
    assert block.file_path == ""


def test_simple_variable_block_parse_variable_name(raw_terraform_block):
    data_block_content = raw_terraform_block("variable/simple_variable.tf", "variable")
    variable_block = VariableBlock()
    variable_block.parse(data_block_content[0], "terraform")
    assert variable_block.variable_name == "key_name"


def test_simple_variable_block_parse_description(raw_terraform_block):
    data_block_content = raw_terraform_block("variable/simple_variable.tf", "variable")
    variable_block = VariableBlock()
    variable_block.parse(data_block_content[0], "terraform")
    assert variable_block.description == "The name of a KMS key"


def test_simple_variable_block_parse_type(raw_terraform_block):
    data_block_content = raw_terraform_block("variable/simple_variable.tf", "variable")
    variable_block = VariableBlock()
    variable_block.parse(data_block_content[0], "terraform")
    assert variable_block.type == "${string}"


def test_simple_variable_block_parse_default(raw_terraform_block):
    data_block_content = raw_terraform_block("variable/simple_variable.tf", "variable")
    variable_block = VariableBlock()
    variable_block.parse(data_block_content[0], "terraform")
    assert variable_block.default == "my-key"


def test_simple_variable_block_parse_validation(raw_terraform_block):
    data_block_content = raw_terraform_block("variable/simple_variable.tf", "variable")
    variable_block = VariableBlock()
    variable_block.parse(data_block_content[0], "terraform")
    assert variable_block.validation == [
        {
            "condition": "${length(var.key_name) > 3}",
            "error_message": "The key name must be at least 4 characters long.",
        }
    ]


def test_simple_variable_block_parse_file_path(raw_terraform_block):
    data_block_content = raw_terraform_block("variable/simple_variable.tf", "variable")
    variable_block = VariableBlock()
    variable_block.parse(data_block_content[0], "terraform")
    assert variable_block.file_path == "terraform"
