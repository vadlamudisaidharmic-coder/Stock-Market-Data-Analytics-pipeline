locals {
  stream_name = "${var.project_name}-stream"

  common_tags = {
    Project   = var.project_name
    ManagedBy = "Terraform"
  }
}