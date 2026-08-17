# Week 2 Day 6 — Weekend Revision Checklist
*Based on today's recall block, Quizlet test, VPC redraw, and error simulation*

---

## ✅ Concepts You Understand Well (don't need much more time here)

### 1. IAM Role vs IAM User — temporary vs permanent credentials
**You showed:** Correctly explained that roles issue temporary, auto-expiring credentials while users have permanent ones, and connected this to *why* it's safer for EC2.
**Why it matters:** This is the #1 security pattern tested in SAA-C03 and used daily by every cloud engineer. It's also the exact reason your `adebola_dev` user needs IAMFullAccess removed before Week 3.

### 2. Least Privilege Principle
**You showed:** Correctly defined it and tied it directly to your own pending security remediation.
**Why it matters:** Core security philosophy behind every IAM decision you'll ever make professionally.

### 3. Why never use root for daily work
**You showed:** Correctly identified the "full unrestricted access if compromised" risk.
**Why it matters:** One of your program's Golden Rules — and a guaranteed interview question.

### 4. Public vs Private Subnet *purpose*
**You showed:** Correctly explained why private/database subnets must stay unreachable (protecting sensitive data).
**Why it matters:** This is the "why" behind every 3-tier architecture you'll design as an architect.

### 5. Three-tier VPC architecture thinking
**You showed:** Added a Database Subnet beyond what the lab even asked for — unprompted, correct instinct.
**Why it matters:** This is architect-level thinking, ahead of where Week 2 expects you to be.

### 6. NACL (subnet-level) vs Security Group (instance-level) — *in your diagram*
**You showed:** Drew NACLs at subnet boundaries and Security Groups closer to resources — correct placement, even though you said it backwards out loud (see below).
**Why it matters:** Your visual instinct is actually ahead of your verbal recall here — worth noticing.

### 7. AccessDenied errors = security working correctly
**You showed:** Correctly identified this isn't a "bug" but least privilege doing its job.
**Why it matters:** Saves you panic during real labs — this error means "fix permissions," not "something is broken."

### 8. `aws configure`, region vs Availability Zone, eu-west-2, GitHub key safety
**You showed:** All answered correctly and confidently.
**Why it matters:** Daily-use fundamentals — these should stay second nature.

---

## 🔴 Concepts to Revise This Weekend (priority order)

### 1. Route Table = what ACTUALLY makes a subnet "public" — **highest priority**
**Where it showed up:** Missed in this morning's recall, missing from your first VPC redraw, and missed again in tonight's exit quiz (you said "Internet Gateway" but forgot the Route Table half twice).
**The fix to remember:** A subnet is public **only** because its route table has a rule: `0.0.0.0/0 → Internet Gateway`. IGW attachment alone does nothing without this.
**Why it matters:** This is one of the most heavily tested VPC concepts in SAA-C03, and the exact scenario from today's Error Simulation.

### 2. Security Group vs NACL — stateful vs stateless (verbal answer was backwards)
**Where it showed up:** You said Security Group = stateless and NACL = stateful — it's the reverse.
**The fix to remember:** Security Group = **stateful** (remembers the connection, auto-allows return traffic). NACL = **stateless** (checks every direction every time, no memory).
**Why it matters:** A classic SAA-C03 trap question — almost guaranteed to appear on your exam.

### 3. Instance Profile — what it actually is
**Where it showed up:** Initially confused it with an S3 "bucket."
**The fix to remember:** It's the wrapper/container that lets an IAM role attach to an EC2 instance (the "lanyard" holding the role's permission contract). AWS Console creates it automatically; CLI/CloudFormation require you to create it explicitly.
**Why it matters:** Comes up any time you're troubleshooting "why can't my EC2 instance use this role."

### 4. NAT Gateway placement
**Where it showed up:** Drew it floating between Private and Public subnets instead of inside the Public Subnet.
**The fix to remember:** NAT Gateway lives **inside the Public Subnet** (it needs a public IP itself) — private subnets route their outbound-only traffic *to* it.
**Why it matters:** Wrong placement is a common real-world misconfiguration that breaks private subnet internet access entirely.

### 5. EC2 CLI command names
**Where it showed up:** Said `launch-instances` and `status-instances` instead of the real commands.
**The fix to remember:** `aws ec2 run-instances` (launch) and `aws ec2 describe-instances --query "..."` (check state).
**Why it matters:** These are hands-on CLI commands you'll type constantly from Week 4 onward.

### 6. Minor recall gaps (quick flashcard fixes)
- Exact policy name: `AmazonEC2ReadOnlyAccess` (you said "read only" — close, but exams want the exact name)
- Homebrew install command: `brew install awscli`

---

## Suggested Weekend Revision Order
1. **Route Table + IGW pairing** (15 min) — re-read the error simulation fix above, then redraw just that one piece from memory
2. **SG vs NACL stateful/stateless** (5 min) — make a single flashcard with the "receptionist who remembers your face vs amnesia checkpoint" analogy
3. **Instance Profile** (5 min) — re-read the lanyard analogy once
4. **NAT Gateway placement** (5 min) — look at one official AWS VPC diagram online and just confirm the box position
5. **CLI command names** (5 min) — drill `run-instances` and `describe-instances` a few times until they're automatic

Total: ~35 minutes, spread however suits you over the weekend.
