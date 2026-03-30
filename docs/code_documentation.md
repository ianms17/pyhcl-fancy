# Code Documentation

## Importing
```python
from pyhcl_fancy.parser.parser import FancyParser
```

## FancyParser
The `FancyParser` class is the primary entry point for PyHCL Fancy. It reads a Terraform
project directory, parses all `.tf` files, and constructs a [Collection Tree](components.md#collection-tree)
representing the project structure and its blocks.

### Initialization
```python
fancy_parser = FancyParser("path/to/terraform")
```

| Parameter | Type | Description |
|---|---|---|
| `terraform_directory` | `str` | Path to the directory containing Terraform files. |

### Attributes

| Attribute | Type | Description |
|---|---|---|
| `terraform_directory` | `str` | The path to the Terraform project directory. |
| `terraform_content` | `dict` | A dictionary mapping file paths to their parsed content. Populated after parsing. |
| `collection_tree` | `CollectionTree` | The Collection Tree built from the parsed Terraform project. |

### `parse()`
The primary API method. Reads all `.tf` files in the directory, constructs an empty tree
from the file paths, then populates the tree with parsed block objects. Local submodule
references are resolved by moving directory nodes under the calling module's file node.

```python
fancy_parser = FancyParser("path/to/terraform")
fancy_parser.parse()
```

## CollectionTree
The `CollectionTree` class holds the tree structure produced by parsing. It is accessible
via `fancy_parser.collection_tree` after calling `parse()`.

### Attributes

| Attribute | Type | Description |
|---|---|---|
| `root` | `Node` | The root node of the tree, representing the top-level Terraform directory. |

### `find_file_node(target_file: str) -> Node`
Searches the tree for a file node matching the given path. Raises `FileNodeNotFoundError`
if the node is not found.

### `find_directory_node(target_directory: str) -> Node`
Searches the tree for a directory node matching the given path. Raises
`DirectoryNodeNotFoundError` if the node is not found.

### `move_node(source: Node, destination: Node, caller: ModuleBlock) -> Node`
Moves a directory node from its current parent to a new destination file node. This is
used internally to reflect local submodule call relationships in the tree. Raises
`InvalidMoveLocationError` if the move is invalid.

### `visualize()`
Prints a visual representation of the tree to the console. Useful for debugging.

```python
fancy_parser = FancyParser("path/to/terraform")
fancy_parser.parse()
fancy_parser.collection_tree.visualize()
```

## Node
Each node in the Collection Tree is an instance of the `Node` class. Nodes represent
either files or directories.

### Attributes

| Attribute | Type | Description |
|---|---|---|
| `blocks` | `list[TerraformBlock]` | List of parsed Terraform blocks (only populated for file nodes). |
| `is_directory` | `bool` | `True` if the node represents a directory. |
| `relative_file_path` | `str` | The relative path of the file or directory. |
| `parent` | `Node` | The parent node in the tree. |
| `children` | `list[Node]` | Child nodes in the tree. |
| `is_root` | `bool` | `True` if this is the root node. |
| `is_leaf` | `bool` | `True` if this node has no children. |
| `submodule_state_path` | `str` | The Terraform state path prefix for blocks within this node's submodule context. |

### `add_child(child: Node) -> None`
Adds a child node and sets its parent reference.

## Blocks
All block classes inherit from `TerraformBlock`, which provides a `file_path` attribute
indicating the source file. Blocks are divided into **Real** and **Reference** categories.

### Real Blocks
Real blocks inherit from `RealBlock`, which adds the following shared attributes:

| Attribute | Type | Description |
|---|---|---|
| `state_path` | `str` | The Terraform state path for the block. |
| `count` | `int` | The `count` meta-argument value, if set. |
| `for_each` | `list \| dict` | The `for_each` meta-argument value, if set. |
| `content` | `dict` | The remaining block attributes as key-value pairs. |

#### ResourceBlock
Represents a `resource` block.

| Attribute | Type | Description |
|---|---|---|
| `resource_type` | `str` | The resource type (e.g., `aws_s3_bucket`). |
| `resource_name` | `str` | The resource name. |

#### ModuleBlock
Represents a `module` block.

| Attribute | Type | Description |
|---|---|---|
| `module_name` | `str` | The module name. |
| `module_source` | `str` | The module source path or registry address. |
| `module_version` | `str` | The module version constraint, if specified. |

#### DataBlock
Represents a `data` block.

| Attribute | Type | Description |
|---|---|---|
| `data_type` | `str` | The data source type (e.g., `aws_iam_policy_document`). |
| `data_name` | `str` | The data source name. |

### Reference Blocks
Reference blocks inherit directly from `TerraformBlock`.

#### VariableBlock
Represents a `variable` block.

| Attribute | Type | Description |
|---|---|---|
| `variable_name` | `str` | The variable name. |
| `description` | `str` | The variable description. |
| `type` | `str` | The variable type constraint. |
| `default` | `Any` | The default value. |
| `validation` | `dict` | Validation rules for the variable. |

#### OutputBlock
Represents an `output` block.

| Attribute | Type | Description |
|---|---|---|
| `name` | `str` | The output name. |
| `value` | `Any` | The output value expression. |
| `description` | `str` | The output description. |
| `options` | `dict` | Additional output options (e.g., `sensitive`). |

#### LocalBlock
Represents a `locals` block.

| Attribute | Type | Description |
|---|---|---|
| `content` | `dict` | Key-value pairs of all local values defined in the block. |

#### ProviderBlock
Represents a `provider` block.

| Attribute | Type | Description |
|---|---|---|
| `type` | `str` | The provider type (e.g., `aws`). |
| `region` | `str` | The provider region. |
| `alias` | `str` | The provider alias, if set. |
| `assume_role` | `dict` | The assume role configuration, if set. |
| `default_tags` | `dict` | Default tags applied to all resources, if set. |
| `options` | `dict` | Any additional provider configuration options. |

#### TerraformMetaBlock
Represents the `terraform` configuration block.

| Attribute | Type | Description |
|---|---|---|
| `backend_type` | `str` | The backend type (e.g., `s3`). |
| `backend_config` | `dict` | The backend configuration options. |
| `required_providers` | `list[dict]` | List of required provider configurations. |
| `options` | `dict` | Additional terraform settings (e.g., `required_version`). |
