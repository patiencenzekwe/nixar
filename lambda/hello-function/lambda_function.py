def lambda_handler(event, context):
    print("Nixar is alive!")
    print("Event received:", event)

    return{
        "statusCode": 200,
        "body": "Hello from Nixar!"
    }