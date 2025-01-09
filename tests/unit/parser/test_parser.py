from pyhcl_fancy.parser.parser import FancyParser


#
# Init
#
def test_fancy_parser_init():
    fancy_parser = FancyParser("./tests/unit/sample_terraform/parser_flat")
    assert (
        fancy_parser.terraform_directory == "./tests/unit/sample_terraform/parser_flat"
    )
    assert fancy_parser.collection_tree.root is None
    assert fancy_parser.terraform_content == {}


#
# Construct Empty Tree
#
def test_construct_empty_tree_root_added(flat_parser):
    flat_parser.construct_empty_tree()
    assert (
        flat_parser.collection_tree.root.relative_file_path
        == "tests/unit/sample_terraform/parser_flat"
    )


def test_construct_empty_tree_all_children_added_to_root_flat(flat_parser):
    flat_parser.construct_empty_tree()
    expected_file_paths = [
        "tests/unit/sample_terraform/parser_flat/data.tf",
        "tests/unit/sample_terraform/parser_flat/locals.tf",
        "tests/unit/sample_terraform/parser_flat/outputs.tf",
        "tests/unit/sample_terraform/parser_flat/provider.tf",
        "tests/unit/sample_terraform/parser_flat/sqs.tf",
        "tests/unit/sample_terraform/parser_flat/terraform.tf",
        "tests/unit/sample_terraform/parser_flat/variables.tf",
        "tests/unit/sample_terraform/parser_flat/lambda.tf",
        "tests/unit/sample_terraform/parser_flat/kms.tf",
    ]

    for child in flat_parser.collection_tree.root.children:
        assert child.relative_file_path in expected_file_paths


def test_construct_empty_tree_all_children_added_to_root_nested(multi_level_parser):
    multi_level_parser.construct_empty_tree()
    expected_file_paths = [
        "tests/unit/sample_terraform/parser_multi_level/data.tf",
        "tests/unit/sample_terraform/parser_multi_level/locals.tf",
        "tests/unit/sample_terraform/parser_multi_level/outputs.tf",
        "tests/unit/sample_terraform/parser_multi_level/provider.tf",
        "tests/unit/sample_terraform/parser_multi_level/sqs.tf",
        "tests/unit/sample_terraform/parser_multi_level/terraform.tf",
        "tests/unit/sample_terraform/parser_multi_level/variables.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda.tf",
        "tests/unit/sample_terraform/parser_multi_level/kms.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda",
    ]

    for child in multi_level_parser.collection_tree.root.children:
        assert child.relative_file_path in expected_file_paths


def test_construct_empty_tree_nested_children_not_added_to_root(multi_level_parser):
    multi_level_parser.construct_empty_tree()
    unexpected_file_paths = [
        "tests/unit/sample_terraform/parser_multi_level/lambda/outputs.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda/variables.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda/main.tf",
    ]

    for child in multi_level_parser.collection_tree.root.children:
        assert child.relative_file_path not in unexpected_file_paths


#
# Set Tree Root
#
def test_set_tree_root_root_added(flat_parser):
    flat_parser._set_tree_root()
    assert flat_parser.collection_tree.root is not None


def test_set_tree_root_root_is_root(flat_parser):
    flat_parser._set_tree_root()
    assert flat_parser.collection_tree.root.is_root


def test_set_tree_root_root_is_directory(flat_parser):
    flat_parser._set_tree_root()
    assert flat_parser.collection_tree.root.is_directory


def test_set_tree_root_root_relative_file_path(flat_parser):
    flat_parser._set_tree_root()
    assert (
        flat_parser.collection_tree.root.relative_file_path
        == "tests/unit/sample_terraform/parser_flat"
    )


def test_set_tree_root_root_submodule_state_path(flat_parser):
    flat_parser._set_tree_root()
    assert flat_parser.collection_tree.root.submodule_state_path == ""


def test_set_tree_root_returns_root(flat_parser):
    root = flat_parser._set_tree_root()
    assert root == flat_parser.collection_tree.root


#
# Parse
#
def test_parse_flat(flat_parser):
    flat_parser.parse()


def test_parse_multi_level(multi_level_parser):
    multi_level_parser.parse()
