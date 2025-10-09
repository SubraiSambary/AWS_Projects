import boto3
import os

def lambda_handler(event, context):
    asg_name = os.environ.get('ASG_NAME', 'test')
    client = boto3.client('autoscaling')

    try:
        client.update_auto_scaling_group(
            AutoScalingGroupName=asg_name,
            DesiredCapacity=2
        )
        print(f"Successfully set desired capacity of {asg_name} to 0")
        return {
            'statusCode': 200,
            'body': f"ASG '{asg_name}' scaled down to 2 instances."
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': f"Error updating ASG: {str(e)}"
        }
