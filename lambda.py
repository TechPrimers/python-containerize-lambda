import json
import boto3

def handler(event, context):
    s3_client = boto3.client('s3')
    s3_clientobj = s3_client.get_object(Bucket='tp-data-bucket', Key='tp-data.txt')

    for line in s3_clientobj['Body'].iter_lines():
        object = json.loads(line)
        print(f"Name: {object['name']['s']} ID: {object['id']['n']}")
    print("Welcome to TechPrimers")
    print("Lambda execution Completed...!")
