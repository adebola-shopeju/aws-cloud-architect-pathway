# W2-D7 Journal — Sunday: Voice Recording & Linux Drill

## What I learned today
- Recorded a 60-second voice explanation of EC2 and VPC, using my own analogies 
  (apartment for EC2, gated estate for VPC, gateman for Security Group). 
  Needed a couple of retakes before it felt clear.
- Ran the full EC2 lifecycle (launch, SSH, stop/start/terminate) and core Linux 
  commands from memory, with no notes.
- Hit a real-world error this morning: AWS CLI rejected a placeholder credential 
  ("exit") instead of my real adebola_dev key. Diagnosed it by checking 
  ~/.aws/credentials directly and fixed it by re-running aws configure.
- Worked through an SSH "Permission denied (publickey)" debugging scenario, and 
  learned the key distinction: "permission denied" = key/auth problem, 
  "timed out" = network/Security Group problem.
- Got my first conceptual introduction to S3 (object storage) and Lambda 
  (serverless, event-triggered compute) ahead of Week 3.

## What was difficult and why
- The IAM Role vs. Instance Profile distinction is still a bit fuzzy — I know 
  instance profile is involved, but I need to be clearer on what the Role 
  itself actually does versus the profile that holds it.
- Lambda didn't click on the first explanation — I needed several simpler, 
  smaller analogies before the "S3 upload triggers Lambda" idea made sense.

## One thing I want to explore further
- How Lambda actually gets connected to a trigger (e.g. an S3 bucket) — 
  the configuration side of it, not just the concept.
