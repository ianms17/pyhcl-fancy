data "aws_caller_identity" "current" {}

data "aws_sqs_queue" "queue" {
    name = "terraform-example-queue.fifo"
}

data "aws_sns_topic" "topic" {
    name = "terraform-example-topic"
}