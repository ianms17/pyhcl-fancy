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
    default_tags {
        tags = {
            "Environment" = "dev"
        }
    }
}

variable "key_name" {
    type = string
    default = "my-key"
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "my-lambda1"
  description   = "My awesome lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.12"

  source_path = "../src/lambda-function1"
}

resource "aws_kms_key" "key" {}

resource "aws_kms_alias" "alias" {
  name          = "alias/my-kms-key"
  target_key_id = aws_kms_key.key.key_id
}

data "aws_sqs_queue" "queue" {
  name = "my-queue"
}

locals {
    queue_name = "my-other-queue"
    lambda_name = "my-other-lambda"
}

output "key_arn" {
    description = "ARN of the KMS key"
    value = aws_kms_key.key.arn
}