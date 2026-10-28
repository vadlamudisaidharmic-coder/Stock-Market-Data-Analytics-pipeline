resource "aws_kinesis_stream" "stock_data" {
  name             = local.stream_name
  shard_count      = 1
  retention_period = 24

  stream_mode_details {
    stream_mode = "PROVISIONED"
  }

  tags = local.common_tags
}
