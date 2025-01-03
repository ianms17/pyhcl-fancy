variable "lambda_reserved_concurrency" {
    type = number
    description = "Reserved concurrency for the lambda function"
    default = 1

    validation {
        condition     = var.lambda_reserved_concurrency > 0
        error_message = "The reserved concurrency must be greater than 0."
    }
}