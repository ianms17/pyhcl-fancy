from pyhcl_fancy.parser.utils import _open_all_tf_files


#
# Flat Repo Tests
#
def test_open_all_tf_files_all_files_added_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    expected_tf_files = [
        "tests/unit/sample_terraform/parser_flat/data.tf",
        "tests/unit/sample_terraform/parser_flat/locals.tf",
        "tests/unit/sample_terraform/parser_flat/outputs.tf",
        "tests/unit/sample_terraform/parser_flat/provider.tf",
        "tests/unit/sample_terraform/parser_flat/sqs.tf",
        "tests/unit/sample_terraform/parser_flat/terraform.tf",
        "tests/unit/sample_terraform/parser_flat/variables.tf",
        "tests/unit/sample_terraform/parser_flat/lambda.tf",
        "tests/unit/sample_terraform/parser_flat/kms.tf"
    ]

    assert set(tf_content.keys()) == set(expected_tf_files)


def test_open_all_tf_files_data_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/data.tf"] ==  {
        "data": [
            {
                "aws_caller_identity": {
                    "current": {}
                }
            },
            {
                "aws_sqs_queue": {
                    "queue": {
                        "name": "terraform-example-queue.fifo"
                    }
                }
            },
            {
                "aws_sns_topic": {
                    "topic": {
                        "name": "terraform-example-topic"
                    }
                }
            }
        ]
    }


def test_open_all_tf_files_kms_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/kms.tf"] ==  {
        "resource": [
            {
                "aws_kms_key": {
                    "key": {}
                }
            },
            {
                "aws_kms_alias": {
                    "alias": {
                        "name": "alias/my-kms-key",
                        "target_key_id": "${aws_kms_key.key.key_id}"
                    }
                }
            }
        ]
    }


def test_open_all_tf_files_lambda_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/lambda.tf"] ==  {
        "module": [
            {
                "lambda_function": {
                    "source": "terraform-aws-modules/lambda/aws",
                    "function_name": "my-lambda1",
                    "description": "My awesome lambda function",
                    "handler": "index.lambda_handler",
                    "runtime": "python3.12",
                    "source_path": "../src/lambda-function1",
                    "reserved_concurrent_executions": "${var.lambda_reserved_concurrency}"
                }
            }
        ]
    }


def test_open_all_tf_files_locals_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/locals.tf"] ==  {
        "locals": [{
            "queue_name": "my-local-queue",
            "lambda_name": "my-local-lambda",
            "key_name": "my-local-key"
        }]
    }


def test_open_all_tf_files_outputs_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/outputs.tf"] ==  {
        "output": [
            {
                "queues": {
                    "description": "Name of the queue",
                    "value": "${aws_sqs_queue.queues[*]}"
                }
            },
            {
                "sourced_topic": {
                    "description": "Data sourced topic",
                    "value": "${data.aws_sns_topic.topic}",
                    "sensitive": False
                }
            }
        ]
    }


def test_open_all_tf_files_provider_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/provider.tf"] ==  {
        "provider": [
            {
                "aws": {
                    "region": "us-east-1",
                    "alias": "primary",
                    "assume_role": [
                        {
                            "role_arn": "arn:aws:iam::123456789012:role/terraform-role"
                        }
                    ],
                    "default_tags": [
                        {
                            "tags": {
                                "Environment": "dev"
                            }
                        }
                    ]
                }
            }
        ]
    }


def test_open_all_tf_files_sqs_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/sqs.tf"] ==  {
        "resource": [
            {
                "aws_sqs_queue": {
                    "count_queues": {
                        "count": 3,
                        "name": "terraform-example-queue-${count.index}.fifo",
                        "fifo_queue": True,
                        "content_based_deduplication": True
                    }
                }
            },
            {
                "aws_sqs_queue": {
                    "for_each_queues": {
                        "for_each": {
                            "queue1": "terraform-example-queue-1.fifo",
                            "queue2": "terraform-example-queue-2.fifo",
                            "queue3": "terraform-example-queue-3.fifo"
                        },
                        "name": "${each.value}",
                        "fifo_queue": True,
                        "content_based_deduplication": True
                    }
                }
            }
        ]
    }


def test_open_all_tf_files_terraform_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/terraform.tf"] ==  {
        "terraform": [
            {
                "required_version": ">= 1.10",
                "required_providers": [
                    {
                        "aws": {
                            "source": "hashicorp/aws",
                            "version": "~> 5.0"
                        }
                    }
                ],
                "backend": [
                    {
                        "s3": {
                            "bucket": "terraform-state-bucket",
                            "key": "terraform.tfstate",
                            "region": "us-east-1"
                        }
                    }
                ]
            }
        ]
    }


def test_open_all_tf_files_variables_flat():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_flat/")
    assert tf_content["tests/unit/sample_terraform/parser_flat/variables.tf"] == {
        "variable": [
            {
                "lambda_name": {
                    "description": "Name of the lambda function",
                    "type": "${string}",
                    "default": "test-lambda"
                }
            },
            {
                "queue_name": {
                    "description": "Name of the queue",
                    "type": "${string}",
                    "default": "test-queue"
                }
            },
            {
                "lambda_reserved_concurrency": {
                    "description": "Reserved concurrency for the lambda function",
                    "type": "${number}",
                    "default": 1,
                    "validation": [
                        {
                            "condition": "${var.lambda_reserved_concurrency > 0}",
                            "error_message": "The reserved concurrency must be greater than 0."
                        }
                    ]
                }
            }
        ]
    }


#
# Multi-Level Repo Tests
#
def test_open_all_tf_files_all_files_added_multi_level():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_multi_level/")
    expected_tf_files = [
        "tests/unit/sample_terraform/parser_multi_level/data.tf",
        "tests/unit/sample_terraform/parser_multi_level/locals.tf",
        "tests/unit/sample_terraform/parser_multi_level/outputs.tf",
        "tests/unit/sample_terraform/parser_multi_level/provider.tf",
        "tests/unit/sample_terraform/parser_multi_level/sqs.tf",
        "tests/unit/sample_terraform/parser_multi_level/terraform.tf",
        "tests/unit/sample_terraform/parser_multi_level/variables.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda.tf",
        "tests/unit/sample_terraform/parser_multi_level/kms.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda/outputs.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda/variables.tf",
        "tests/unit/sample_terraform/parser_multi_level/lambda/main.tf"
    ]

    assert set(tf_content.keys()) == set(expected_tf_files)


def test_open_all_tf_files_lambda_multi_level():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_multi_level/")
    assert tf_content["tests/unit/sample_terraform/parser_multi_level/lambda.tf"] ==  {
        "module": [
            {
                "lambda_function": {
                    "source": "./lambda",
                    "lambda_reserved_concurrency": "${var.lambda_reserved_concurrency}"
                }
            }
        ]
    }


def test_open_all_tf_files_lambda_module_main_multi_level():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_multi_level/")
    assert tf_content["tests/unit/sample_terraform/parser_multi_level/lambda/main.tf"] ==  {
        "module": [
            {
                "lambda_function": {
                    "source": "terraform-aws-modules/lambda/aws",
                    "function_name": "my-lambda1",
                    "description": "My awesome lambda function",
                    "handler": "index.lambda_handler",
                    "runtime": "python3.12",
                    "source_path": "../src/lambda-function1",
                    "reserved_concurrent_executions": "${var.lambda_reserved_concurrency}"
                }
            }
        ]
    }


def test_open_all_tf_files_lambda_module_outputs_multi_level():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_multi_level/")
    assert tf_content["tests/unit/sample_terraform/parser_multi_level/lambda/outputs.tf"] ==  {
        "output": [
            {
                "lambda_arn": {
                    "description": "ARN of the lambda function",
                    "value": "${module.lambda_function.lambda_arn}"
                }
            }
        ]
    }


def test_open_all_tf_files_lambda_module_variables_multi_level():
    tf_content = _open_all_tf_files("./tests/unit/sample_terraform/parser_multi_level/")
    assert tf_content["tests/unit/sample_terraform/parser_multi_level/lambda/variables.tf"] ==  {
        "variable": [
            {
                "lambda_reserved_concurrency": {
                    "description": "Reserved concurrency for the lambda function",
                    "type": "${number}",
                    "default": 1,
                    "validation": [
                        {
                            "condition": "${var.lambda_reserved_concurrency > 0}",
                            "error_message": "The reserved concurrency must be greater than 0."
                        }
                    ]
                }
            }
        ]
    }