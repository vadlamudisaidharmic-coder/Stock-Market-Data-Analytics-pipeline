output "kinesis_stream_name" {
  value = aws_kinesis_stream.stock_data.name
}

output "kinesis_stream_arn" {
  value = aws_kinesis_stream.stock_data.arn
}