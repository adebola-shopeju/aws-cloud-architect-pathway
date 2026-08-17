# W6-D1 Journal — ALB Fundamentals
**Date:** Monday, 13 July 2026
**Session:** 13:00 – ~16:45
**Week:** 6 · Day 1
**Confidence rating:** 4/5

---

## What I built today

A fully working, health-checked, two-AZ web tier on AWS — the foundation pattern behind every production web application.

```
[ Browser / Internet ]
         |
         | HTTP:80
         ▼
[ week6-alb ]  ←  Active, internet-facing
         |
         | forwards to
         ▼
[ week6-target-group ]  ←  health check: GET / every 30s
         |
    _____|_____
   |           |
   ▼           ▼
[week6-web-server-1]    [week6-web-server-2]
  eu-west-2a               eu-west-2b
  Running ✅               Running ✅
  Healthy ✅               Healthy ✅
```

---

## Pre-flight fixes (before labs started)

Before touching any lab, I had to fix three things in the existing Week 5 VPC:

1. **Missing second public subnet** — both existing subnets were in `eu-west-2a`. An ALB requires at least two subnets in two different AZs. Created `week5-public-subnet-2b` (CIDR: `10.1.3.0/24`) in `eu-west-2b`.
2. **Auto-assign public IPv4 was OFF** on the new subnet — enabled it so EC2 instances get public IPs automatically.
3. **Wrong route table** — the new subnet inherited the main (default) route table which had no IGW route. Associated it with `rtb-0ea42e0322996d610`, the existing public route table that already had the IGW route.

**Key lesson:** Always check subnet → route table → IGW chain before building. A subnet is only truly "public" if all three are in place.

---

## Lab 1 — Two EC2 instances + Target Group

### Instances launched

| Instance | ID | AZ | Subnet |
|---|---|---|---|
| week6-web-server-1 | i-0941e9e009d34ddc3 | eu-west-2a | week5-public-subnet-test |
| week6-web-server-2 | i-0f09f9133c3c42499 | eu-west-2b | week5-public-subnet-2b |

- AMI: Amazon Linux 2023
- Instance type: t3.micro
- Security group: `week6-alb-sg` (HTTP:80 from 0.0.0.0/0, SSH:22 from My IP)
- User data: installed httpd, created index.html showing hostname and AZ

### Target group created

- Name: `week6-target-group`
- Protocol: HTTP · Port: 80
- VPC: week5-adebola-test-vpc
- Health check: HTTP on path `/`
- Both instances registered as targets

---

## Lab 2 — ALB creation + traffic verification

### ALB created

- Name: `week6-alb`
- Scheme: Internet-facing
- IP type: IPv4
- Subnets: week5-public-subnet-test (eu-west-2a) + week5-public-subnet-2b (eu-west-2b)
- Security group: week6-alb-sg
- Listener: HTTP:80 → forward to week6-target-group
- DNS: `week6-alb-350768148.eu-west-2.elb.amazonaws.com`

### Traffic distribution verified

Refreshing the ALB DNS name in the browser alternated between:
- `Hello from ip-10-1-1-134.eu-west-2.compute.internal - Instance 1 - AZ: eu-west-2a`
- `Hello from ip-10-1-3-11.eu-west-2.compute.internal - Instance 2 - AZ: eu-west-2b`

**This proved the ALB was distributing traffic across both AZs.**

---

## Error simulation — unhealthy targets

Changed the HTTP:80 inbound rule on `week6-alb-sg` from `0.0.0.0/0` to `My IP only`.

Result within 30–60 seconds:
- Healthy: **0**
- Unhealthy: **2**

Both EC2 instances were still **running** — the virtual machines were on. But the ALB's health check traffic (which comes from AWS internal IPs, not my IP) was blocked by the security group. The ALB marked both targets unhealthy and stopped routing traffic to them.

Fixed by changing the rule back to `0.0.0.0/0`. Both targets returned to healthy within 60 seconds.

**Key lesson:** "Running" ≠ "Healthy." Check the security group before anything else when targets go unhealthy.

---

## Concepts learned today

**Listener** — the process on the ALB watching a specific port/protocol for incoming requests. Today: HTTP:80. Once a request arrives, the listener evaluates its rules and forwards to a target group.

**Target group** — a named list of EC2 instances (or IPs, or Lambda functions) the ALB can send traffic to. Every target group has a health check configuration.

**Health check** — the ALB's automatic probe sent to every registered target on a schedule. Today: GET / on HTTP every 30 seconds. Miss the threshold → target flips to unhealthy → removed from rotation immediately.

**Running vs Healthy** — Running means the EC2 VM is switched on. Healthy means the web server inside it is answering the ALB's health check with HTTP 200 OK. You can have one without the other.

**AZ spread** — placing instances in different Availability Zones. If one entire AZ goes down, the ALB's node in the surviving AZ keeps serving traffic to healthy targets there.

**503 Service Unavailable** — what users see when the ALB has zero healthy targets.

---

## Production security group pattern (learned today)

In production, ALB and instances should have **separate** security groups:

```
Internet → ALB-sg (port 80 from 0.0.0.0/0)
ALB-sg   → Instance-sg (port 80 from ALB-sg only)
```

This means instances are never directly reachable from the internet — all traffic must pass through the ALB first. Today's lab used one shared security group for simplicity.

---

## Evidence screenshots

All screenshots in: `week6/labs/W6-D1/`

| File | What it shows |
|---|---|
| W6-D1-new-subnet-2b.png | New subnet created in eu-west-2b |
| W6-D1-both-instances-running.png | Both EC2 instances running |
| W6-D1-target-group-created.png | Target group created |
| W6-D1-alb-active.png | ALB in Active state |
| W6-D1-targets-healthy.png | Both targets healthy |
| W6-D1-alb-instance1-response.png | Browser showing Instance 1 response |
| W6-D1-alb-instance2-response.png | Browser showing Instance 2 response |
| W6-D1-targets-unhealthy.png | Both targets unhealthy (error sim) |
| W6-D1-targets-health-restored.png | Both targets healthy again |

---

## Commit

```
W6-D1: ALB fundamentals --- built ALB with target group across two AZs, verified traffic distribution and health check simulation
```

---

## Tomorrow — W6-D2 (Tuesday)

Advanced routing on top of today's ALB — path-based routing rules so different URLs (`/api`, `/images`) go to different target groups. Today's ALB and target group stay running and become the foundation.
