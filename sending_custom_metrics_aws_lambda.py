# sending custom metrics using aws lambda 
import boto3
import random

def lambda_handler(event, context):


    # creating cloud watch client to send metric data
    cloudwatch = boto3.client('cloudwatch')

    response = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': 'KPIs',
                'Dimensions': [
                    {
                        'Name': 'PURCHASES_SERVICE',
                        'Value': 'CoolService'
                    },
                    {
                        'Name': 'APP_VERSION',
                        'Value': '1.0'
                    },
                ],
                'Unit': 'None',
                'Value': random.randint(1, 500)
            },
        ],
        Namespace='CoolApp'
    )

    print(response)