#!/bin/bash

# EC2 Lifecycle Script
# W2-D4: Launch, stop, start, terminate an EC2 instance

# Variables - edit these before running
AMI_ID="ami-0b4f5712d8c11fe5c"
INSTANCE_TYPE="t3.micro"
KEY_NAME="week2-key"
SG_ID="YOUR-SG-ID"
SUBNET_ID="YOUR-SUBNET-ID"

# Launch instance
echo "Launching EC2 instance..."
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id $AMI_ID \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-group-ids $SG_ID \
  --subnet-id $SUBNET_ID \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=cli-launched-demo}]' \
  --query 'Instances[0].InstanceId' \
  --output text)

echo "Launched: $INSTANCE_ID"
