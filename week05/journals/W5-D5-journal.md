# Week 5 · Day 5 — Full VPC Integration: Bastion Access, NACLs, and Config

**Date:** July 12, 2026

## What I built
- Launched a private EC2 instance (`10.1.2.39`) with no public IP, in
  `week5-private-subnet-test`
- Set up SSH agent forwarding (`ssh-add` + `ssh -A`) to reach the
  private instance through the public EC2 acting as a bastion host
- Verified outbound-only internet access from the private instance via
  the NAT Gateway (`curl -I https://aws.amazon.com` → HTTP 200)
- Built a custom Network ACL (`week5-private-nacl`) from scratch and
  associated it with the private subnet
- Configured inbound rules (SSH from bastion, deliberate deny on port
  8080, ephemeral return-traffic allow, general VPC allow) and
  outbound rules (internal VPC replies, HTTP/HTTPS, ephemeral ports)
- Proved the deny rule works: `curl` to port 8080 timed out (`curl:
  (28) Connection timed out`) instead of connecting
- Verified the AWS Config `restricted-ssh` rule (set up Thursday) is
  live and compliant — all 9 Security Groups in the account passing,
  including the one edited today

## What I learned
- A bastion host is just a public-facing instance you hop through to
  reach a private one — SSH agent forwarding (`-A`) is what lets your
  local key authenticate the second hop without ever copying the key
  onto either server.
- NACLs are stateless — unlike Security Groups, inbound and outbound
  rules are evaluated completely independently. An allow rule in one
  direction does not automatically permit the reply in the other.
- This bit me directly: I allowed HTTPS out to the internet but hadn't
  opened the matching inbound ephemeral port range (1024–65535), so
  the reply had nowhere to come back in. The request left fine — the
  `curl` just hung until it timed out.
- A NACL deny rule shows up as a silent timeout, not an error. An
  instant "connection refused" usually just means nothing is listening
  on that port locally — it never means the NACL blocked it. Only a
  timeout run *across the subnet boundary* is real evidence the deny
  rule is doing its job.
- AWS Config doesn't block traffic — it's a passive compliance watcher
  running continuously in the background, checking every matching
  resource against a rule and marking it compliant or not, regardless
  of whether the resource is still reachable.
- Security Groups can self-reference — "allow traffic from anything
  that has this same SG attached" is the standard way to let instances
  in the same tier reach each other without hardcoding IPs.

## Where I got stuck (and fixed)
- Tried to SSH into the private instance from my local Mac directly —
  doesn't work, since the private IP isn't routable from outside the
  VPC. Had to go through the public EC2 first.
- First hop attempt failed silently (`ssh-add -L` showed "no
  identities") — the key wasn't loaded into the local agent before
  connecting with `-A`, so there was nothing to forward.
- Lost track of which machine I was on more than once after a dropped
  SSH session — learned to check the shell prompt every time before
  running a command.
- First hop to the private EC2 froze entirely — turned out the private
  instance's Security Group only allowed SSH from my home IP, not from
  traffic originating inside the VPC. Fixed with a self-referencing SG
  rule.
- Missed the outbound-ephemeral-ports NACL rule initially, causing the
  same "silent freeze" pattern on the `curl` test — added rule 250 to
  fix it.
- Accidentally tested the port-8080 deny rule from the private
  instance to itself instead of from the public EC2 across the subnet
  boundary — got an instant refusal instead of the expected timeout,
  which turned out to be the wrong test entirely.

## Real-world relevance
- Bastion hosts + private subnets are the standard pattern for
  production databases and internal services — nothing sensitive gets
  a public IP, but authorized admins can still reach it through one
  hardened, monitored entry point.
- Layered security (Security Group + NACL + Config monitoring) means
  no single misconfiguration exposes the whole system — this is
  "defense in depth" in practice, not just a buzzword.

## Self-rating
Overall: **4/5** — built and proved out the full bastion → NAT →
NACL → Config chain end to end tonight, including catching and fixing
three separate misconfigurations through debugging rather than being
told the answer. NACL statelessness is solid; want to revisit the
Security Group vs. NACL evaluation order cold in a future session
before calling it a 5.

## Next session
- Concept-check questions held over from tonight (NACL rule ordering,
  the "why deny rules matter" reasoning) — revisit at the start of the
  next session
- Week 5 wrap-up: Turing.com profile review, final architecture
  diagram, Feynman-style recap of the full week
- Cost hygiene cleanup for tonight's resources (private EC2, NAT
  Gateway, Elastic IP, custom NACL) before next session begins
