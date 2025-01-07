module "lambda_function" {
  source = "./lambda"
  lambda_reserved_concurrency = var.lambda_reserved_concurrency
}