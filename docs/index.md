# Welcome to PyHCL Fancy
PyHCL Fancy is a rich parser for HCL Terraform that converts an IaC configuration project
into a computer friendly tree-like structure. From this structure comes more automation
opportunities that will allow developers to rework and reimagine Terraform however they
may wish.


## Getting Started

### Installation
PyHCL Fancy is installable via pip and requires a minimum Python version of 3.10 to be used.

```
pip install pyhcl-fancy
```

### Import and Use
PyHCL Fancy has a simple to use, developer friendly interface that only requires one API
call to generate Collection Tree of all of your Terraform files and their composite blocks.

```
from pyhcl_fancy.parser.parser import FancyParser

fancy_parser = FancyParser("path/to/terraform")
fancy_parser.parse()
```

## Learn More
### Understand the Components
Read more about the individual components that are generated via parsing: [Components](components.md)

### Code Documentation
Read more about the functionality of the code: [Docs](documentation.md)

### Find Us
* GitHub: [https://github.com/ianms17/pyhcl-fancy](https://github.com/ianms17/pyhcl-fancy)
* PyPI: [https://pypi.org/project/pyhcl-fancy/](https://pypi.org/project/pyhcl-fancy/)
