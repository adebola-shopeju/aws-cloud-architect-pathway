1. What is boto3?
"boto3 is the AWS SDK for Python. It lets Python scripts talk to AWS services so you can automate tasks like listing, launching, and terminating EC2 instances without touching the console."

2. CLI vs Python automation
"The CLI is for typing one command at a time manually in the terminal. boto3 lets you embed AWS actions inside Python logic — loops, conditions, decisions — so you can automate complex tasks the CLI alone cannot do."

3. boto3.client('ec2')
boto3.client('ec2', region_name='eu-west-2') is like picking up a phone and dialling AWS EC2 in London. After that line, ec2 is your open line to that service.
"boto3.client('ec2') opens a connection to the EC2 service in a specific AWS region. It's like dialling AWS London — after that line, you can make API calls through that connection."

4. What surprised you
"I was surprised that the CLI has limits. I assumed it could automate anything, but today I understood that Python gives you logic — conditions and loops — which the CLI alone doesn't have."

5. Open questions
"I want to explore more boto3 functions beyond describe and terminate — things like launching instances from code, working with S3, and automating IAM tasks."