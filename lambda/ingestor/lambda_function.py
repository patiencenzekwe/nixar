import json
import base64
import boto3

comprehend = boto3.client('comprehend', region_name='eu-west-2')

def lambda_handler(event, context):
    print("Ingestor triggered by Kinesis")
    
    results = []
    
    for record in event['Records']:
        try:
            payload = base64.b64decode(record['kinesis']['data'])
            data = json.loads(payload.decode('utf-8'))
            
            topic = data.get('topic')
            text = data.get('text')
            
            print(f"Analysing topic: {topic}")
            print(f"Text: {text}")
            
            response = comprehend.detect_sentiment(
                Text=text,
                LanguageCode='en'
            )
            
            sentiment = response['Sentiment']
            scores = response['SentimentScore']
            
            print(f"Sentiment: {sentiment}")
            print(f"Scores: {scores}")
            
            result = {
                "topic": topic,
                "text": text,
                "sentiment": sentiment,
                "positive": round(scores['Positive'], 4),
                "negative": round(scores['Negative'], 4),
                "neutral": round(scores['Neutral'], 4),
                "mixed": round(scores['Mixed'], 4)
            }
            
            results.append(result)
            print("Result:", result)
            
        except Exception as e:
            print("Error processing record:", str(e))
    
    return {
        "statusCode": 200,
        "body": f"Processed {len(results)} records"
    }