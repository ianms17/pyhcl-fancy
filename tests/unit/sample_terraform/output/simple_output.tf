output "key_arn" {
    description = "ARN of the KMS key"
    value = aws_kms_key.key.arn
    sensitive = false
}