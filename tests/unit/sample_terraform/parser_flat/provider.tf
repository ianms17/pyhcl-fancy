provider "aws" {
    region = "us-east-1"
    alias = "primary"
    assume_role {
        role_arn = "arn:aws:iam::123456789012:role/terraform-role"
    }
    default_tags {
        tags = {
            "Environment" = "dev"
        }
    }
}