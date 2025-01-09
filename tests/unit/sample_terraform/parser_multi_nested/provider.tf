terraform {
    required_version = ">= 1.10"
    backend "s3" {
        bucket = "terraform-state-bucket"
        key    = "terraform.tfstate"
        region = "us-east-1"
    }
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 5.0"
        }
    }
}

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