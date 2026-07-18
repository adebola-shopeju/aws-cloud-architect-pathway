# W6-D6 Journal --- AWS Security Fundamentals & Route 53 Routing Policies

**Date:** Saturday, 18 July 2026 **Session:** \~13:00 -- \~16:30
**Week:** 6 · Day 6 **Confidence rating:** 5/5

------------------------------------------------------------------------

## What I learned today

Today's session was a theory and revision day focused on AWS security
fundamentals and Amazon Route 53 routing policies. Unlike previous days,
there were no infrastructure labs or AWS resources to deploy. Instead,
the goal was to understand the security principles behind AWS and how
Route 53 intelligently routes users to applications.

By the end of today's session, I was able to explain the AWS Shared
Responsibility Model, identify the purpose of five core AWS security
services, compare four Route 53 routing policies, create a comprehensive
revision flashcard deck, and successfully complete a knowledge
assessment.

------------------------------------------------------------------------

## Topic 1 --- AWS Shared Responsibility Model

### Security OF the Cloud (AWS)

AWS is responsible for securing the cloud infrastructure itself,
including:

-   Physical data centers
-   Physical servers
-   Networking infrastructure
-   Hardware
-   Physical security

### Security IN the Cloud (Customer)

Customers are responsible for securing the resources they deploy inside
AWS, including:

-   IAM users and permissions
-   Customer data
-   Security Groups
-   Applications
-   EC2 operating system updates
-   Network configuration

### Key lesson

> AWS secures the cloud.\
> I secure everything I build inside the cloud.

------------------------------------------------------------------------

## Shared Responsibility Diagram

                     AWS CLOUD
                        |
            ----------------------------
            |                          |
            ▼                          ▼

     SECURITY OF THE CLOUD       SECURITY IN THE CLOUD
            AWS                     Customer

     Data Centers              IAM Users
     Hardware                  Applications
     Networking                Customer Data
     Physical Security         Security Groups
                                EC2 OS Updates

------------------------------------------------------------------------

## Topic 2 --- AWS Security Services

-   **Amazon GuardDuty** --- Detects suspicious activity and potential
    security threats.
-   **Amazon Inspector** --- Scans AWS workloads for vulnerabilities.
-   **Amazon Macie** --- Finds sensitive information stored in Amazon
    S3.
-   **AWS Shield** --- Protects applications against DDoS attacks.
-   **AWS Artifact** --- Provides AWS compliance reports and
    certifications.

------------------------------------------------------------------------

## Topic 3 --- Amazon Route 53 Routing Policies

### Failover Routing

Automatically redirects users to a backup resource when the primary
resource becomes unavailable.

### Weighted Routing

Distributes traffic between resources according to assigned percentages.

### Latency-Based Routing

Routes users to the AWS Region with the fastest response time.

### Geolocation Routing

Routes users according to their geographic location.

------------------------------------------------------------------------

## Flashcard Revision

Created **71 flashcards** covering:

-   ALB
-   ASG
-   AWS Systems Manager
-   Shared Responsibility Model
-   AWS Security Services
-   Route 53 Routing Policies

------------------------------------------------------------------------

## Practice Assessment

**Score:** **10/10 (100%)**

------------------------------------------------------------------------

## Key Concepts Learned Today

-   Shared Responsibility Model
-   Amazon GuardDuty
-   Amazon Inspector
-   Amazon Macie
-   AWS Shield
-   AWS Artifact
-   Failover Routing
-   Weighted Routing
-   Latency-Based Routing
-   Geolocation Routing

------------------------------------------------------------------------

## Evidence Produced

-   Shared Responsibility Model diagram
-   Four Route 53 routing diagrams
-   71 flashcards
-   Practice assessment (10/10)

------------------------------------------------------------------------

## Commit

``` bash
git add .

git commit -m "W6-D6: AWS security fundamentals and Route 53 routing policies"

git push origin main
```

------------------------------------------------------------------------

## Tomorrow --- Week 7 Day 1

Hands-on AWS learning resumes with new infrastructure topics building on
the security and networking concepts covered today.
