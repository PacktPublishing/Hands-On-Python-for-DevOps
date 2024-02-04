import boto3
import datetime

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Current time is: {current_time}")
    instance_id = 'i-07e253eb7f6f0aeed'
    
    if current_time >= '00:00:00' and current_time <= '03:59:59':
        print("Starting EC2 instance...")
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"EC2 instance {instance_id} started.")
    elif current_time >= '04:00:00' and current_time <= '23:59:59':
        print("Stopping EC2 instance...")
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"EC2 instance {instance_id} stopped.")
    else:
        print("Not within the scheduled time window.")
