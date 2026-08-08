# AWS Cloud Architect Pathway
### Adebola Shopeju · CloudOps · 2026

> Building production-grade AWS skills in public every lab, every mistake, every fix committed here.

---

## Certification Track

| Cert | Status | Target |
|------|--------|--------|
| AWS Cloud Practitioner (CLF-C02) | 🟡 In progress | Month 2 (Week 8) |
| AWS AI Practitioner (AIF-C01) | ⬜ Upcoming | Month 3 (Week 12) |
| AWS Solutions Architect Associate (SAA-C03) | ⬜ Upcoming | Month 6 (Week 26) |

---

## Program Overview

**6 months, 34h/week intensive** run by CloudOps, designed for the remote cloud job market.

| | |
|---|---|
| **Daily schedule** | Monday–Friday 12:00–6:00pm WAT + Saturday & Sunday deep dives |
| **Primary region** | eu-west-2 (London) |
| **Target roles** | Junior Cloud Engineer · Cloud Support · DevOps Engineer (Remote) |

---

## What I'm Building

Each week produces real, committed evidence not just notes.

- **Infrastructure labs** — VPC, EC2, IAM, S3, ALB, Auto Scaling, RDS, EKS
- **Automation scripts** — Python (boto3), AWS CLI, Bash
- **IaC** — Terraform (including remote state with S3 + DynamoDB locking)
- **CI/CD pipelines** — CodePipeline → CodeBuild → CodeDeploy → EKS
- **Security** — IAM least privilege, GuardDuty, WAF, Macie, Secrets Manager
- **FinOps** — Cost Explorer, Savings Plans, budget alerts, Cost Anomaly Detection
- **Architecture diagrams** — draw.io, committed weekly

---

## Repo Structure

Each week follows the same pattern: `journals/` and `labs/` always present; `scripts/` and `iam-policies/` added only when that week's work needs them.
```
aws-cloud-architect-pathway/
├── week1/
│   ├── journals/        # daily learning logs
│   └── labs/            # screenshots and lab outputs
├── week2/
│   ├── journals/
│   ├── labs/
│   └── scripts/         # Python and bash scripts
├── week3/
│   ├── journals/
│   ├── labs/
│   ├── scripts/
│   └── iam-policies/    # least privilege policy JSON files
├── week4/
│   ├── journals/
│   └── labs/
├── week5/
│   ├── journals/
│   ├── labs/            # per-day subfolders: W5-D1/ through W5-D5/
│   └── scripts/
└── .gitignore           # AWS credentials never committed
```

---

## Progress Log

| Week | Focus | Key Output |
|------|-------|------------|
| W1 | Git · Linux · IAM basics | IAM group + CLI configured |
| W2 | EC2 · VPC · SSH | EC2 lifecycle lab · week2-vpc (10.0.0.0/16) |
| W3 | Python · boto3 · IAM policies | EC2 automation script · IAM least privilege remediation |
| W4 | S3 · versioning · static hosting | Secrets Manager · Parameter Store |
| W5 | VPC deep-dive · NAT · NACLs · AWS Config | Full VPC integration: bastion host access, custom NACL with deny rule, AWS Config compliance monitoring |
| W6 | SSM Agent · ALB · Auto Scaling · AWS Config | Advanced ALB routing, Auto Scaling Group, AWS Config change tracking |
| W7 | CloudFront · CDN · SQS | CloudFront distribution with S3 origin + OAC, cache behaviors, geo-restriction · SQS standard queue with DLQ (max receives = 3) · case study: "VPC + Config + Security" |
| W8 | CloudFront · OAC · SQS · exam prep | Static site behind CloudFront with Origin Access Control · 4 timed CLF-C02 mocks · CLF-C02 certified |
## Month 1 Summary

Four weeks in. Git and GitHub for version control, IAM for least-privilege access, EC2 for compute, a custom VPC for networking, S3 for storage (versioning + static hosting), and Secrets Manager / Parameter Store for configuration and secrets management.

- Static site live: [S3 website endpoint](http://adebola-w4d3-static-site.s3-website.eu-west-2.amazonaws.com)
- Full write-up: [My first month learning AWS](https://lnkd.in/eGXvqKG5)
- 35+ Quizlet cards, daily journals, and lab screenshots committed for every session

## Month 2 Kickoff

Week 5 marked a shift from individual services to full integration building a production-style VPC end to end rather than isolated pieces.

- Public and private subnets, NAT Gateway, and route tables working together as a real network, not just   individual labs
- Bastion host access pattern: reaching a private, non internet facing instance safely through a public    jump box with SSH agent forwarding
- Custom Network ACLs with deliberate deny rules proven working, not just configured, by testing both      the allow and block paths
- AWS Config actively monitoring Security Group compliance across the account, continuously, in the        background

Month 2 moves into Load Balancers, Auto Scaling, and Systems Manager building on this networking foundation rather than starting fresh.

## Month 2 Summary

Eight weeks in, and Cloud Practitioner (CLF-C02) is certified.

- **Networking depth** — SSM Agent for keyless access, Application Load
  Balancer with path-based routing and sticky sessions, Auto Scaling
  Groups keeping instance count aligned to demand
- **Delivery and content** — CloudFront in front of S3, locked down with
  Origin Access Control so the bucket is only reachable through the
  distribution, not directly
- **Messaging** — SQS with visibility timeouts, long polling, and
  dead-letter queues for reliable async processing
- **Security and billing** — Support tiers, Shared Responsibility Model,
  Well-Architected Framework's 6 pillars, Trusted Advisor cost checks
- **Exam prep** — 4 timed mock exams, missed-question drilling by domain,
  real exam sat and passed
- Full write-up: [Passed AWS Cloud Practitioner](#) *(add LinkedIn post link)*

Month 3 moves into AI Practitioner (AIF-C01) prep, running alongside
Solutions Architect Associate (SAA-C03) as parallel "flavor" content.

---

## Core Principles

**Security first** — `adebola_dev` runs with least privilege. Root is never used for daily work. No credentials ever committed.

**Build in public** — every lab is committed with a structured message: `W[X]-D[N]: topic --- what was built`. Evidence screenshots are saved for portfolio use.

**eu-west-2 only** — all lab work runs in London region. Resources are deleted after every session to protect free tier credits.

---
## Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/adebola-shopeju)
- 📬 Open to junior cloud engineer, cloud support, and DevOps roles
