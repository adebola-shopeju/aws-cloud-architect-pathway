# Week 1 Summary — AWS Cloud Architect Program
**Program:** CloudOps Nigeria Remote-First AWS Cloud Architect Program
**GitHub:** adebola-shopeju
**Period:** Week 1 — Git, Linux, IAM, Cloud Concepts

---

## Git & GitHub
Git is a version control system that lives on your local machine. It tracks changes to files over time and saves snapshots (called commits) only when you decide to save them. GitHub is the cloud archive where all commits are stored permanently and shared with the world.

- `git init` — initialises a new local repository
- `git add .` — moves changes to the staging area
- `git commit -m "message"` — snapshots staged changes to local repo
- `git push` — sends commits to GitHub
- `git pull` — fetches and merges changes from GitHub
- `git branch branch-name` — creates a new branch
- `git merge branch-name` — merges a branch into main
- `git status` — shows current state of working tree
- `git log` — shows commit history
- Commit message format used: `W[X]-D[N]: topic --- what was built`

---

## Linux Fundamentals
Linux is the language every AWS EC2 server speaks. Mastery of Linux navigation, file management, and permissions is a core requirement for any cloud engineer.

- `pwd` — print working directory (where am I?)
- `ls` — list files in current directory
- `ls -la` — list all files including hidden, with full details
- `cd folder` — change directory
- `mkdir folder` — create a new directory
- `touch file.txt` — create a new empty file
- `cat file.txt` — display file contents
- `cp file destination` — copy a file
- `mv file destination` — move or rename a file
- `rm file` — delete a file
- `chmod 755 file` — set permissions (owner: rwx, group: r-x, others: r-x)
- `chmod 644 file` — owner: rw-, group: r--, others: r--
- `chmod 600 file` — owner: rw-, group: none, others: none (private files)
- Permission string breakdown: `-rwxr-xr--` = type + owner + group + others

---

## IAM & AWS CLI
IAM (Identity and Access Management) is the control panel that manages who can access what inside your AWS account. The AWS CLI is a tool that lets you control AWS directly from your terminal using typed commands instead of clicking through the console.

- **IAM User** — an individual identity for a person or application
- **IAM Group** — a collection of users; attach a policy once and all users inherit it
- **IAM Policy** — a JSON document defining Effect (Allow/Deny), Action, and Resource
- **Least Privilege** — give users only the permissions they absolutely need, nothing more
- **Root account** — the master account; must be secured with MFA and never used daily
- `aws configure` — sets up CLI with Access Key, Secret Key, Region, and output format
- `aws iam list-users` — lists all IAM users in the account
- `aws sts get-caller-identity` — confirms which identity is currently active in CLI
- Evidence screenshot naming convention: `W[week]-D[day]-[description].png`

---

## Cloud Concepts
AWS global infrastructure is built around Regions and Availability Zones to ensure high availability and fault tolerance.

- **Region** — a geographical area containing multiple Availability Zones (e.g. London = `eu-west-2`)
- **Availability Zone (AZ)** — one or more physical data centres within a Region, with independent power, cooling, and networking
- **AZ examples in London:** `eu-west-2a`, `eu-west-2b`, `eu-west-2c`
- **Shared Responsibility Model** — AWS secures the cloud (hardware, network, hypervisors, physical facilities); the customer secures what is in the cloud (data, IAM, OS on EC2, encryption)
- **Budget Alert** — set a $10 billing alert in AWS Console to avoid surprise charges
- AZs are physically separated to protect against flood, fire, and power failure

---

## Labs Completed
- Day 1: Git init, first commit, push to GitHub, branching and merging, conflict resolution
- Day 2: Linux navigation, chmod permissions, shell scripting, Git/GitHub troubleshooting
- Day 3: IAM user and group creation, policy attachment, AWS CLI installation and configuration
- Day 4: Cloud concepts, Shared Responsibility Model, budget alert setup

---

## Key Commands Quick Reference
```bash
# Git
git init
git add .
git commit -m "message"
git push
git pull
git status
git log

# Linux
ls -la
chmod 755 filename
cat filename
mkdir foldername

# AWS CLI
aws configure
aws iam list-users
aws sts get-caller-identity
```

---

*Week 1 complete. Foundation built: version control, Linux, IAM security, and AWS global infrastructure.*