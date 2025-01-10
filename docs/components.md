# Parser Output
The following is a list of the primary components that are generated during parsing.

## Collection Tree
The Collection Tree is the primary data structure that gets generated during parsing.

It is a tree structure that represents the files that make up a Terraform project.
Each node in the tree represents either a directory in the project, or a `*.tf` file.

The tree does differ from a traditional filesystem hierarchy, however, as a node's
parent is determined 

### Example Collection Tree
The following example is generated from a sample Terraform project and created using the
Collection Tree's visualize functionality.
```
terraform
|   terraform/main.tf
|   |   terraform/lambda
|   |   |   terraform/lambda/main.tf
|   |   |   terraform/lambda/variables.tf
|   |   terraform/sqs
|   |   |   terraform/sqs/main.tf
|   |   |   terraform/sqs/variables.tf
|   terraform/variables.tf
|   terraform/outputs.tf
|   terraform/providers.tf
```
_Note: The following example illustrates a Terraform project with a main.tf file that makes_
_calls to the locally defined submodules in the lambda and sqs directories._


## Nodes
Nodes in the Collection Tree are representations of either files, or directories. In the example
above, each line in the output is a node. If a line ends in `.tf`, it's a file node, otherwise it's
a directory node.

Each file node contains a set of blocks, which are described in more detail [here](#blocks).

## Blocks
Blocks refer to the standard Terraform blocks that make a `.tf` file. All the different block types
are shown below. The block types are segmented into _Real_ and _Reference_. Real blocks are blocks
that are used to define real infrastructure that is deployed by Terraform. Reference blocks refer
to the pieces that Terraform uses to configure how the resources will be deployed.

### Real
#### Resource
Resource blocks define individual resources that are deployed by Terraform. These are things like an
AWS KMS Key, or singular S3 Bucket.

#### Module
Module blocks are abstractions that are made up of any combination of underlying blocks. For example,
a KMS module that defines both a KMS Key and its associated alias, without the need to directly
configure both resources directly.

#### Data
Data blocks are used to find real infrastructure that has already been deployed to the cloud.

### Reference
#### Variable
Variable blocks are used to create variables that can then be referenced elsewhere in the
Terraform.

#### Output
Output blocks can be used for one of two things. Within a module, outputs can define attributes
that are accessible externally via the output name. Outside of a module, outputs can be used to
print specified values to the console during the `terraform apply`.

#### Local
Local blocks are manually-defined constant values that are accessible by other blocks. 

#### Provider
The provider block defines the configuration that tells Terraform where to deploy resources to, and
gives information to define how it will get permission to do so. Provider versions are also defined here.

#### Terraform Meta
The Terraform Meta block defines the Terraform version, the providers that must be defined, and a few
other details that configure how Terraform will be used in the project.
