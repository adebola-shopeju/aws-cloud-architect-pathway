SSM Session Manager

Today I learned that there is a more secure and modern alternative to SSH for accessing EC2 instances. Instead of opening port 22 and managing .pem key files, AWS Systems Manager Session Manager allows engineers to connect to EC2 instances directly through the AWS Console without any inbound ports open.

Session Manager works because the SSM Agent a small program pre-installed on Amazon Linux 2 runs inside the EC2 instance and makes a constant outbound connection to AWS Systems Manager. When I click Connect in the console, my session travels through that existing outbound tunnel. No SSH client. No key pair. No open ports.

I created an IAM Role called SSM-EC2-Role with the AmazonSSMManagedInstanceCore policy and attached it to a new EC2 instance called week3-ssm-demo running in week2-vpc. I then connected through Session Manager and confirmed I was inside the instance by running whoami which returned ssm-user and hostname, which showed ip-10-0-1-157.eu-west-2.compute.internal.

The biggest surprise today was discovering that the terminal does not have to live on my Mac. The entire shell session ran inside my browser, served securely through AWS. This is the standard used by engineers at UK banks and healthcare companies where port 22 is permanently banned.