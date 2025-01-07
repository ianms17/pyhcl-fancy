from pyhcl_fancy.blocks.real.module.module_block import ModuleBlock


def test_module_block_init():
    module_block = ModuleBlock()
    assert module_block.module_name == ""
    assert module_block.module_source == ""
    assert module_block.module_version == ""
    assert module_block.content == {}
    assert module_block.state_path == ""
    assert module_block.count is None
    assert module_block.for_each is None
    assert module_block.file_path == ""


def test_module_block_parse_module_name(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.module_name == "lambda_function"


def test_module_block_parse_module_source(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.module_source == "terraform-aws-modules/lambda/aws"


def test_module_block_parse_module_version(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.module_version == ""


def test_module_block_parse_content(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.content == {
        "function_name": "my-lambda1",
        "description": "My awesome lambda function",
        "handler": "index.lambda_handler",
        "runtime": "python3.12",
        "source_path": "../src/lambda-function1"
    }


def test_module_block_parse_state_path(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.state_path == "module.lambda_function"


def test_module_block_parse_file_path(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.file_path == "terraform"


def test_module_block_parse_count(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.count is None


def test_module_block_parse_for_each(raw_terraform_block, sample_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()
    module_block.parse(raw_module_dict[0], "terraform", sample_file_node)
    assert module_block.for_each is None


def test_module_block_parse_state_path_nested_module(raw_terraform_block, submodule_file_node):
    raw_module_dict = raw_terraform_block("module/simple_module.tf", "module")
    module_block = ModuleBlock()    
    module_block.parse(raw_module_dict[0], "terraform", submodule_file_node)
    assert module_block.state_path == "module.test_module.module.lambda_function"