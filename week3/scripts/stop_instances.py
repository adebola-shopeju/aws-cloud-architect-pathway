import boto3

ec2 = boto3.client('ec2', region_name='eu-west-2')
response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        if state == 'running':
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopped: {instance_id}")