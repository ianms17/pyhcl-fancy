# Code Documentation
## Importing
```
from pyhcl_fancy.parser.parser import FancyParser
```

## Parser
The `parse` API is the primary way to interact with PyHCL Fancy.
With a single function, developers can read a Terraform project
into the [Collection Tree](components.md/#collection-tree).
```
fancy_parser = FancyParser("path/to/terraform")
fancy_parser.parse()
```

## Visualizer
The visualizer can be used to output the tree structure to the
console. This was built for debugging, but feel free to use it
for whatever you wish.
```
fancy_parser = FancyParser("path/to/terraform")
fancy_parser.parse()
fancy_parser.collection_tree.visualize()
```