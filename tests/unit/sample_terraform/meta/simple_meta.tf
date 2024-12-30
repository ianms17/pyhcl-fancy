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