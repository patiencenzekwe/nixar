# Nixar Infrastructure

## AWS Region
eu-west-2 (London)

## Resources Created

### IAM
- Role: nixar-lambda-role
- Policy: AWSLambdaBasicExecutionRole
- Policy: AWSLambdaKinesisExecutionRole
- Policy: ComprehendReadOnly
- Purpose: Least privilege execution role for all Nixar Lambda functions

### Lambda
- Function: nixar-hello
- Runtime: Python 3.14
- Purpose: Entry point test function

### Kinesis
- Stream: nixar-sentiment-stream
- Shards: 1
- Retention: 24 hours
- Purpose: Real-time data pipeline between producers and consumers

### Event Source Mapping
- Trigger: nixar-sentiment-stream
- Consumer: nixar-ingestor
- Batch size: 10
- Starting position: LATEST
- Purpose: Automatically triggers Lambda when data arrives on stream

### Comprehend
- Service: Amazon Comprehend
- Region: eu-west-2
- Purpose: NLP sentiment analysis of topic text returning positive, negative, neutral and mixed scores
- Language: English