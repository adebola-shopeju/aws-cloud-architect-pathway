import boto3

# Create EC2 client (London region)
ec2 = boto3.client('ec2', region_name='eu-west-2')

# Call describe_instances API
response = ec2.describe_instances()

print("EC2 instances in eu-west-2:\n")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        print(f"ID: {instance_id} | State: {state}")

        # Terminate if running
        if state == 'running':
            print(f"  → Terminating {instance_id}...")
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"  → Terminated.")