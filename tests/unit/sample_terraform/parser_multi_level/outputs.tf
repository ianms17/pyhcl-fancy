output "queues" {
    description = "Name of the queue"
    value = aws_sqs_queue.queues[*]
}

output "sourced_topic" {
    description = "Data sourced topic"
    value = data.aws_sns_topic.topic
    sensitive = false
}