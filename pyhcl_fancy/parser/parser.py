from pyhcl_fancy.collection_tree.node import Node
from pyhcl_fancy.collection_tree.tree import CollectionTree

from pyhcl_fancy.blocks.real.data.data_block import DataBlock
from pyhcl_fancy.blocks.real.module.module_block import ModuleBlock
from pyhcl_fancy.blocks.real.resource.resource_block import ResourceBlock
from pyhcl_fancy.blocks.reference.meta.meta_block import TerraformMetaBlock
from pyhcl_fancy.blocks.reference.output.output_block import OutputBlock
from pyhcl_fancy.blocks.reference.provider.provider_block import ProviderBlock
from pyhcl_fancy.blocks.reference.local.local_block import LocalBlock
from pyhcl_fancy.blocks.reference.variable.variable_block import VariableBlock

from pyhcl_fancy.parser.utils import _open_all_tf_files


class FancyParser:
    def __init__(self, terraform_directory: str):
        self.terraform_directory = terraform_directory
        self.terraform_content: dict = {}
        self.collection_tree: CollectionTree = CollectionTree()

    def read_tf_files(self) -> None:
        self.terraform_content = _open_all_tf_files(self.terraform_directory)

    def set_tree_root(self) -> Node:
        root = Node()
        root.is_root = True
        root.is_directory = True
        root.relative_file_path = self.terraform_directory
        return self.collection_tree.add_root(root)

    def _parse_module_block(self, module_block: ModuleBlock) -> None:
        pass

    def _parse_resource_block(self, resource_block: ResourceBlock) -> None:
        pass

    def _parse_data_block(self, data_block: DataBlock) -> None:
        pass

    def _parse_meta_block(self, meta_block: TerraformMetaBlock) -> None:
        pass

    def _parse_output_block(self, output_block: OutputBlock) -> None:
        pass

    def _parse_provider_block(self, provider_block: ProviderBlock) -> None:
        pass

    def _parse_local_block(self, local_block: LocalBlock) -> None:
        pass

    def _parse_variable_block(self, variable_block: VariableBlock) -> None:
        pass
