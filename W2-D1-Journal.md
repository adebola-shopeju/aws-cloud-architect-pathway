# W2-D1: EC2 Launch & SSH Access

## What I built today
- Launched my first EC2 instance (t3.micro) named `week2-web-server` in eu-west-2 (London)
- Created a key pair (`week2-key.pem`) and secured it with `chmod 400`
- Configured a Security Group allowing SSH only from My IP (port 22)
- Successfully connected to a live AWS server via SSH from my MacBook

## What I learned
- EC2 is a rentable virtual server in the cloud — no physical hardware needed
- AMI is the blueprint/template of the server (Amazon Linux 2023)
- Instance type determines the size and power (t3.micro = studio flat)
- Security Group = doorman controlling who can knock (network level)
- Key Pair = physical key proving your identity (authentication level)
- `chmod 400` locks the .pem file so only I can read it — SSH requires this
- SSH creates an encrypted tunnel between my terminal and the cloud server

## Commands used inside EC2
- `whoami` — confirmed ec2-user
- `hostname` — ip-172-31-14-236.eu-west-2.compute.internal
- `free -h` — 916MB RAM, 123MB used
- `df -h` — 8GB disk, 20% used
- `uptime` — server running 16 minutes

## Evidence
- W2-D1-EC2-launch-success.png
- W2-D1-SSH-success.png

## Confidence sentence
Today I launched a real cloud server and connected to it from my terminal. I am doing cloud engineering.
