variable "key_name" {
    type = string
    description = "The name of a KMS key"
    default = "my-key"

    validation {
        condition     = length(var.key_name) > 3
        error_message = "The key name must be at least 4 characters long."
    }
}