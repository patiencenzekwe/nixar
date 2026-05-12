# Nixar Infrastructure

## AWS Region
eu-west-2 (London)

## Resources Created

### IAM
- Role: nixar-lambda-role
- Policy: AWSLambdaBasicExecutionRole

### Lambda
- Function: nixar-hello
- Runtime: Python 3.14
- Purpose: Entry point test function

### Kinesis
- Stream: nixar-sentiment-stream
- Shards: 1
- Retention: 24 hours
- Purpose: Real-time data pipeline between producers and consumers