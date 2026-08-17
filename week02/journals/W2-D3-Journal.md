# W2-D3 Journal — Security Groups & IAM Roles

## Date: 17 June 2026

## What I Built Today
- Created a Security Group `week2-sg-secure` with SSH restricted to My IP only
- Created an IAM Role `EC2-S3-ReadOnly-Role` with S3 read-only permissions
- Launched EC2 instance with both Security Group and IAM Role attached
- SSH'd into EC2 and verified role was working via `aws sts get-caller-identity`
- Ran `aws s3 ls` successfully without any access keys configured

## Key Concepts Learned

### Security Groups
A Security Group is a virtual firewall that controls inbound and outbound traffic to an EC2 instance. It is stateful — meaning if traffic is allowed in, the response is automatically allowed out.

### IAM Roles
An IAM Role gives an AWS resource like EC2 a temporary identity and permissions without storing any access keys. It consists of two parts:
- Trust Policy — decides WHO can use the role
- Permissions Policy — decides WHAT the role can do

### Why Roles Are Safer Than Access Keys
Access keys are permanent and can be leaked via code or logs. IAM Roles provide temporary credentials that rotate automatically — nothing to store, nothing to leak.

## Evidence
- sg-rules.png
- iam-role-created.png
- ec2-launch-success.png
- iam-role-working.png