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
                            module_block = ModuleBlock()
                            module_block.parse(
                                raw_module_dict=module,
                                module_file_path=file
                            )
                            file_node.blocks.append(module_block)

                        # module source points to a submodule, move that submodules directory node to the calling module's file node
                        if Path(module_block.module_source).is_dir():
                            submodule_directory_node = self.collection_tree.find_directory_node(self.collection_tree.root, module_block.module_source)
                            self.collection_tree.move_node(submodule_directory_node, file_node, module_block)

                    case "resource":
                        for resource in self.terraform_content[file][block_type]:
                            resource_block = ResourceBlock()
                            resource_block.parse(
                                raw_resource_dict=resource,
                                resource_file_path=file
                            )
                            file_node.blocks.append(resource_block)
                    case "data":
                        for data in self.terraform_content[file][block_type]:
                            data_block = DataBlock()
                            data_block.parse(
                                raw_data_dict=data,
                                data_file_path=file,
                                parent_file_node=file_node
                            )
                            file_node.blocks.append(data_block)
                    case "output":
                        for output in self.terraform_content[file][block_type]:
                            output_block = OutputBlock()
                            output_block.parse(
                                raw_output_dict=output,
                                output_file_path=file
                            )
                            file_node.blocks.append(output_block)
                    case "variable":
                        for variable in self.terraform_content[file][block_type]:
                            variable_block = VariableBlock()
                            variable_block.parse(
                                raw_variable_dict=variable,
                                variable_file_path=file
                            )
                            file_node.blocks.append(variable_block)
                    case "local":
                        local_block = LocalBlock()
                        local_block.parse(
                            raw_locals_dict=self.terraform_content[file][block_type],
                            locals_file_path=file
                        )
                        file_node.blocks.append(local_block)
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
        root.submodule_state_path = ""
        root.relative_file_path = self.terraform_directory
        return self.collection_tree.add_root(root)
