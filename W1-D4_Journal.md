# W1-D4 Journal — Cloud Concepts & Console Mastery
**Date:** 11 June 2026
**Program:** CloudOps Nigeria AWS Cloud Architect Program

## What I Learned Today

**Regions** — A geographical area with data centers, made up of multiple Availability Zones. Most countries have their own Region with 2-5 AZs for high availability, so that in cases of fire, flood, electrical and other unforeseen outbreaks, AWS users have backup.

**Edge Locations** — Also known as CloudFront cache points. Allows data to be readily available with low latency so users get their data faster without delay.

**Shared Responsibility Model** — A division of labour. AWS manages security OF the cloud (data centers, network, hypervisors). The customer manages security IN the cloud (passwords, IAM, encryption).

**Console Navigation** — A user-friendly interface that allows users to interact with AWS without needing the Command Line Interface. Same results, more accessible.

**Budget Alerts** — Set to ensure users are alerted before their resources exceed their budget. Email alerts notify you in time so you can stop or pause resources before hitting the limit.

## What Was Difficult

Realising that I needed to log into my root user account to give my adebola_dev account access to IAM billing, and also allow adebola_dev to have access to AWS Budgets. The two-step fix (master switch + Billing policy) was not obvious at first.

## One Thing I Want to Explore Further

How to fully use the AWS Console — there are many services I have not explored yet.
