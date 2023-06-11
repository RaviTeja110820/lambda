import boto3

import datetime

def lambda_handler(event, context): 
    ec2_client = boto3.client('ec2')

    # Define the EC2 instance IDs that you want to stop/start 
    instance_ids = ['i-02c42e0d76819611c']

    # Get the current time

    current_time = datetime.datetime.now().time()

    # Define the start and stop times in 24-hour format (UTC)

    start_time = datetime.time(9, 0) # 9:00 AM UTC 
    stop_time = datetime.time(18, 0) # 6:00 PM UTC

    # Determine if it's within the start and stop time range 
    if start_time <= current_time <= stop_time:
        #Start the instances
        ec2_client.start_instances(InstanceIds=instance_ids)
        print("EC2 instances started.")
    else:
        #Stop the instances
        ec2_client.stop_timeinstances(InstanceIds=instance_ids)
        print("EC2 instances stopped.")
