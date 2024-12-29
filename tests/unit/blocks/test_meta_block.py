from pyhcl_fancy.blocks.reference.meta.meta_block import TerraformMetaBlock


def test_terraform_meta_block_init():
    meta_block = TerraformMetaBlock()
    assert meta_block.backend_type == ""
    assert meta_block.backend_config == {}
    assert meta_block.required_providers == []
    assert meta_block.options == {}


def test_terraform_meta_block_parse_backend_type(basic_parsed_terraform):
    meta_block_content = basic_parsed_terraform["terraform"]
    meta_block = TerraformMetaBlock()
    meta_block.parse(meta_block_content[0], "terraform")
    assert meta_block.backend_type == "s3"


def test_terraform_meta_block_parse_backend_config(basic_parsed_terraform):
    meta_block_content = basic_parsed_terraform["terraform"]
    meta_block = TerraformMetaBlock()
    meta_block.parse(meta_block_content[0], "terraform")
    assert meta_block.backend_config == {
        "bucket": "terraform-state-bucket",
        "key": "terraform.tfstate",
        "region": "us-east-1"
    }


def test_terraform_meta_block_parse_required_providers(basic_parsed_terraform):
    meta_block_content = basic_parsed_terraform["terraform"]
    meta_block = TerraformMetaBlock()
    meta_block.parse(meta_block_content[0], "terraform")
    assert meta_block.required_providers == [
        {
            "aws": {
                "source": "hashicorp/aws",
                "version": "~> 5.0"
            }
        }
    ]


def test_terraform_meta_block_parse_options(basic_parsed_terraform):
    meta_block_content = basic_parsed_terraform["terraform"]
    meta_block = TerraformMetaBlock()
    meta_block.parse(meta_block_content[0], "terraform")
    assert meta_block.options == {
        "required_version": ">= 1.10"
    }


def test_terraform_meta_block_parse_file_path(basic_parsed_terraform):
    meta_block_content = basic_parsed_terraform["terraform"]
    meta_block = TerraformMetaBlock()
    meta_block.parse(meta_block_content[0], "terraform")
    assert meta_block.file_path == "terraform"