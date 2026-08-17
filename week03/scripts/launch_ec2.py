import boto3

# Create a connection to EC2 in eu-west-2
ec2 = boto3.client('ec2', region_name='eu-west-2')

# Launch one EC2 instance
response = ec2.run_instances(
    ImageId='ami-0b9d0e17ab4360618',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1
)

# Pull the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance launched: {instance_id}")

# Create a waiter and wait until the instance is running
waiter = ec2.get_waiter('instance_running')
print("Waiting for instance to be running...")
waiter.wait(InstanceIds=[instance_id])

print(f"Instance {instance_id} is now RUNNING.")