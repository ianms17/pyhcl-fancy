output "lambda_arn" {
    description = "ARN of the lambda function"
    value = module.lambda_function.lambda_arn
}