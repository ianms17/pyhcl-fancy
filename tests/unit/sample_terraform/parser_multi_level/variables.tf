variable "lambda_name" {
    type = string
    description = "Name of the lambda function"
    default = "test-lambda"
}

variable "queue_name" {
    type = string
    description = "Name of the queue"
    default = "test-queue"
}

variable "lambda_reserved_concurrency" {
    type = number
    description = "Reserved concurrency for the lambda function"
    default = 1

    validation {
        condition     = var.lambda_reserved_concurrency > 0
        error_message = "The reserved concurrency must be greater than 0."
    }
}