import json
import base64

def lambda_handler(event, context):
    print("Ingestor triggered by Kinesis")
    
    for record in event['Records']:
        try:
            payload = base64.b64decode(record['kinesis']['data'])
            data = json.loads(payload.decode('utf-8'))
            
            print("Record received:", data)
            print("Topic to analyse:", data.get('topic'))
            
        except Exception as e:
            print("Error processing record:", str(e))
            print("Raw payload:", record['kinesis']['data'])
    
    return {
        "statusCode": 200,
        "body": f"Processed {len(event['Records'])} records"
    }