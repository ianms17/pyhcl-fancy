from pyhcl_fancy.blocks.reference.provider.provider_block import ProviderBlock


def test_provider_block_init():
    provider_block = ProviderBlock()
    assert provider_block.type == ""
    assert provider_block.region == ""
    assert provider_block.alias == ""
    assert provider_block.assume_role == {}
    assert provider_block.default_tags == {}
    assert provider_block.options == {}
    assert provider_block.file_path == ""


def test_provider_block_parse_type(basic_parsed_terraform):
    provider_block_content = basic_parsed_terraform["provider"]
    provider_block = ProviderBlock()
    provider_block.parse(provider_block_content[0], "terraform")
    assert provider_block.type == "aws"


def test_provider_block_parse_region(basic_parsed_terraform):
    provider_block_content = basic_parsed_terraform["provider"]
    provider_block = ProviderBlock()
    provider_block.parse(provider_block_content[0], "terraform")
    assert provider_block.region == "us-east-1"


def test_provider_block_parse_alias(basic_parsed_terraform):
    provider_block_content = basic_parsed_terraform["provider"]
    provider_block = ProviderBlock()
    provider_block.parse(provider_block_content[0], "terraform")
    assert provider_block.alias == "primary"


def test_provider_block_parse_assume_role(basic_parsed_terraform):
    provider_block_content = basic_parsed_terraform["provider"]
    provider_block = ProviderBlock()
    provider_block.parse(provider_block_content[0], "terraform")
    assert provider_block.assume_role == {
        "role_arn": "arn:aws:iam::123456789012:role/terraform-role"
    }


def test_provider_block_parse_default_tags(basic_parsed_terraform):
    provider_block_content = basic_parsed_terraform["provider"]
    provider_block = ProviderBlock()
    provider_block.parse(provider_block_content[0], "terraform")
    assert provider_block.default_tags == {
        "Environment": "dev"
    }


def test_provider_block_parse_options(basic_parsed_terraform):
    provider_block_content = basic_parsed_terraform["provider"]
    provider_block = ProviderBlock()
    provider_block.parse(provider_block_content[0], "terraform")
    assert provider_block.options == {}