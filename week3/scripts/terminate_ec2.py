import boto3

# Create a connection to EC2 in eu-west-2
ec2 = boto3.client('ec2', region_name='eu-west-2')

# The instance ID we want to terminate
instance_id = 'i-082dce0ed4f7afa20'

# Terminate the instance
print(f"Terminating instance: {instance_id}")
ec2.terminate_instances(InstanceIds=[instance_id])

# Wait until the instance is fully terminated
waiter = ec2.get_waiter('instance_terminated')
print("Waiting for instance to terminate...")
waiter.wait(InstanceIds=[instance_id])

print(f"Instance {instance_id} is now TERMINATED. Resources released.")