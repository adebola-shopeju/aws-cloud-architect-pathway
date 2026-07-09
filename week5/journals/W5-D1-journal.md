# Week 5 · Day 1 — VPC Fundamentals

**Date:** July 9, 2026

## What I built
- Custom VPC (`10.0.0.0/16`)
- Public subnet (`10.0.1.0/24`, eu-west-2a) and private subnet
  (`10.0.2.0/24`, eu-west-2b)
- Internet Gateway, attached to the VPC
- Public route table with a `0.0.0.0/0 → IGW` route, associated only
  with the public subnet
- Verified everything independently using the AWS CLI
  (`describe-vpcs`, `describe-subnets`, `describe-route-tables`)

## What I learned
- CIDR notation: the number after the `/` tells you how many bits are
  fixed — more fixed bits = smaller, more specific address range.
  `/16` = big pool (65,536), `/24` = smaller slice (256, 251 usable
  after AWS reserves 5).
- A subnet's CIDR must share the VPC's fixed prefix to "fit" inside it
  — e.g. anything starting `10.0.x.x` fits inside a `10.0.0.0/16` VPC.
- Every route table auto-includes a `local` route for traffic staying
  inside the VPC — that's why subnets can always talk to each other by
  default.
- Attaching an Internet Gateway to a VPC does nothing by itself — a
  subnet only becomes "public" once its route table has a
  `0.0.0.0/0 → IGW` route AND the subnet is associated with that table.
- `0.0.0.0/0` is the least specific possible route ("everywhere") —
  more specific routes always win over it.
- Multi-AZ placement (public in 2a, private in 2b) protects against a
  single Availability Zone outage.

## Where I got stuck (and fixed)
- Mixed up `/16` vs `/24` — which one is "bigger" in terms of address
  count. Fixed by working through the actual division (65,536 ÷ 4,096
  = 16 subnets vs 65,536 ÷ 256 = 256 subnets).
- Flipped the "does this CIDR fit inside the VPC" rule at first, then
  corrected it and re-confirmed with a different VPC range
  (`172.20.0.0/16`).
- Mixed up which CIDR filter (`vpc-id` vs `tag:Name`) narrows to one
  resource vs a whole group — corrected and confirmed.

## Real-world cost lesson
- Found a leftover NAT Gateway + Elastic IP from a previous session,
  both quietly capable of running up charges. Practiced the full
  cleanup order: delete NAT Gateway → release Elastic IP → delete VPC.

## Self-rating
Overall: **4/5** — solid working understanding of CIDR math, subnet
design, IGW/route table mechanics, and CLI verification. Not yet a
"zero hesitation" 5 — worth revisiting cold in a future session.

## Next session
- Lab: Error Simulation (from today's study guide, not yet started)
- Remote track: start Turing.com profile
- Eventually: NAT Gateway for private subnet outbound-only internet
  access (Week 5 topic, deliberately skipped today)
