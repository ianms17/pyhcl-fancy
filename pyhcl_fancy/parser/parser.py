from pathlib import Path

from pyhcl_fancy.collection_tree.node import Node
from pyhcl_fancy.collection_tree.tree import CollectionTree
from pyhcl_fancy.collection_tree.exceptions import DirectoryNodeNotFoundError

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


    def construct_empty_tree(self) -> CollectionTree:
        """
        Constructs an empty collection tree from the Terraform files.

        Iterates through the Terraform content, setting up the directory
        and file nodes in the collection tree. It initializes the root node
        and adds directory and file nodes based on the file paths in the
        Terraform content. If a directory node is not found, it creates a new
        one and adds it to the collection tree.

        Returns:
            CollectionTree: The constructed collection tree with directory
            and file nodes added.
        """

        root = self._set_tree_root()

        for file in self.terraform_content:
            # if file path minus file name is the given directory, file is root level
            if "/".join(file.split("/")[:-1]) == self.terraform_directory:
                directory_node = root
            else:
                try:
                    # directory path is everything but the last element
                    directory_path = file.split("/")[:-1]
                    directory_node = self.collection_tree.find_directory_node(root, directory_path)
                # if directory node isn't found, create it
                except DirectoryNodeNotFoundError:
                    directory_node = Node()
                    directory_node.is_directory = True
                    directory_node.relative_file_path = "/".join(directory_path)
                    directory_node.parent = root
                    root.add_child(directory_node)

            # add the file node to the directory node
            file_node = Node()
            file_node.relative_file_path = file
            directory_node.add_child(file_node)
            
        

    
    def parse(self):
        # preprocess
        self._read_tf_files()
        self.construct_empty_tree()

        for file in self.terraform_content:
            file_node = self.collection_tree.find_file_node(self.collection_tree.root, file)
            
            for block_type in self.terraform_content[file]:
                # switch case to apply a ruleset based on the type of block
                match block_type:
                    case "module":
                        for module in self.terraform_content[file][block_type]:
                            module_block = self._parse_module_block(
                                module_name=module,
                                module_file_path=file,
                                module_content=self.terraform_content[file][block_type][module],
                            )
                            file_node.blocks.append(module_block)

                        # module source points to a submodule, move that submodules directory node to the calling module's file node
                        if Path(module_block.module_source).is_dir():
                            submodule_directory_node = self.collection_tree.find_directory_node(self.collection_tree.root, module_block.module_source)
                            self.collection_tree.move_node(submodule_directory_node, file_node)

                    case "resource":
                        continue
                    case "data":
                        continue
                    case "output":
                        continue
                    case "variable":
                        continue
                    case "local":
                        continue
                    case "provider":
                        continue
                    case "terraform":
                        continue
                    


    def _read_tf_files(self) -> None:
        self.terraform_content = _open_all_tf_files(self.terraform_directory)

    def _set_tree_root(self) -> Node:
        root = Node()
        root.is_root = True
        root.is_directory = True
        root.relative_file_path = self.terraform_directory
        return self.collection_tree.add_root(root)

    def _parse_module_block(self, module_name: str, module_file_path: str, module_content: dict) -> ModuleBlock:
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
