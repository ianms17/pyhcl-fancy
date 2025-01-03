resource "aws_sqs_queue" "count_queues" {
    count = 3
    name  = "terraform-example-queue-${count.index}.fifo"
    fifo_queue                  = true
    content_based_deduplication = true
}

resource "aws_sqs_queue" "for_each_queues" {
    for_each = {
        "queue1" = "terraform-example-queue-1.fifo"
        "queue2" = "terraform-example-queue-2.fifo"
        "queue3" = "terraform-example-queue-3.fifo"
    }
    name  = each.value
    fifo_queue                  = true
    content_based_deduplication = true
}