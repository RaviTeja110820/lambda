import boto3
import datetime

ec2 = boto3.client('ec2', region_name='ap-south-1')

def lambda_handler(event, context):
    instance_id = 'i-076cf799ef3dfa540'
    
    current_time_utc = datetime.datetime.utcnow()
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    current_time_ist = current_time_utc + ist_offset
    print('current time: {}'.format(current_time_ist))
    
    
    if current_time_ist.hour >= 9 and current_time_ist.hour < 18 :
        # Start the instance
        ec2.start_instances(InstanceIds=[instance_id])
        print('Instance started: {}'.format(instance_id))
    else:
        # Stop the instance
        ec2.stop_instances(InstanceIds=[instance_id])
        print('Instance stopped: {}'.format(instance_id))

