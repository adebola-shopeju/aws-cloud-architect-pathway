# AWS Cloud Architect Pathway
### Adebola Shopeju · CloudOps · 2026

> Building production-grade AWS skills in public — every lab, every mistake, every fix committed here.

---

## Certification Track

| Cert | Status | Target |
|------|--------|--------|
| AWS Cloud Practitioner (CLF-C02) | 🟡 In progress | Month 2 (Week 8) |
| AWS AI Practitioner (AIF-C01) | ⬜ Upcoming | Month 3 (Week 12) |
| AWS Solutions Architect Associate (SAA-C03) | ⬜ Upcoming | Month 6 (Week 26) |

---

## Program Overview

**6-month, 34h/week intensive** run by CloudOps, designed for the remote cloud job market.

| | |
|---|---|
| **Daily schedule** | Monday–Friday 12:00–6:00pm WAT + Saturday & Sunday deep dives |
| **Primary region** | eu-west-2 (London) |
| **Target roles** | Junior Cloud Engineer · Cloud Support · DevOps Engineer (Remote) |

---

## What I'm Building

Each week produces real, committed evidence — not just notes.

- **Infrastructure labs** — VPC, EC2, IAM, S3, ALB, Auto Scaling, RDS, EKS
- **Automation scripts** — Python (boto3), AWS CLI, Bash
- **IaC** — Terraform (including remote state with S3 + DynamoDB locking)
- **CI/CD pipelines** — CodePipeline → CodeBuild → CodeDeploy → EKS
- **Security** — IAM least privilege, GuardDuty, WAF, Macie, Secrets Manager
- **FinOps** — Cost Explorer, Savings Plans, budget alerts, Cost Anomaly Detection
- **Architecture diagrams** — draw.io, committed weekly

---

## Repo Structure

```
aws-cloud-architect-pathway/
├── week1/
│   ├── journals/        # daily learning logs
│   ├── labs/            # screenshots and lab outputs
│   └── scripts/         # Python and bash scripts
├── week2/
│   └── ...
├── week3/
│   ├── journals/
│   ├── labs/
│   ├── scripts/
│   └── iam-policies/    # least privilege policy JSON files
├── evidence/            # key screenshots for portfolio use
└── .gitignore           # AWS credentials never committed
```

---

## Progress Log

| Week | Focus | Key Output |
|------|-------|------------|
| W1 | Git · Linux · IAM basics | IAM group + CLI configured |
| W2 | EC2 · VPC · SSH | EC2 lifecycle lab · week2-vpc (10.0.0.0/16) |
| W3 | Python · boto3 · IAM policies | EC2 automation script · IAM least privilege remediation |
| W4 | S3 · versioning · static hosting | *(upcoming)* |

---

## Core Principles

**Security first** — `adebola_dev` runs with least privilege. Root is never used for daily work. No credentials ever committed.

**Build in public** — every lab is committed with a structured message: `W[X]-D[N]: topic --- what was built`. Evidence screenshots are saved for portfolio use.

**eu-west-2 only** — all lab work runs in London region. Resources are deleted after every session to protect free tier credits.

---

## Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/adebola-shopeju)
- 📬 Open to junior cloud engineer, cloud support, and DevOps roles
