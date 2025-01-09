module "lambda" {
    source = "aws-terraform-modules/lambda/aws"
    lambda_name = var.lambda_name
    runtime = "python3.9"
    handler = "index.handler"
}

module "sns" {
    source = "../sns"
    topic_name = "test-topic"
}

module "sqs" {
    source = "../sqs"
    queue_name = "test-queue"
}