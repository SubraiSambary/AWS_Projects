## Project Overview

The purpose of this project is to demonstrate how to design and deploy a simple three-tier application architecture on AWS while also showcasing automation using serverless services. The project helps learners:
- Understand core AWS services such as VPC, EC2, S3, CloudFront, RDS, DynamoDB, IAM, and Route 53.
- Learn how to host and serve a static website with HTML and connect it to a backend (PHP page on EC2).
- Explore AWS automation by using Lambda and EventBridge to automatically start an EC2 instance on a schedule.
- Practice implementing networking, security, and monitoring best practices as per AWS Solutions Architect Associate-level knowledge.

This project acts as a hands-on learning guide for beginners who want to build AWS projects from scratch, without CloudFormation or automation scripts, focusing entirely on manual configuration to strengthen their fundamentals.



## Learning Objectives
By the end of this project, learners will be able to not only deploy resources but also appreciate the architectural decisions behind them:
- Networking & Security → How to design a VPC with public/private subnets, Internet Gateway, NAT Gateway, and Security Groups that balance accessibility with security.
- Compute & Storage → Best practices in deploying EC2 with EBS/EFS for persistence, and how to differentiate their use cases.
- Application Hosting → Hosting a static HTML front-end while serving dynamic content from a PHP-based backend on EC2, connected securely to RDS MySQL for relational data and DynamoDB for NoSQL use cases.
- Automation & Scalability → Leveraging Auto Scaling with ELB for high availability and using Lambda + EventBridge to automate scheduled EC2 operations.
- DNS & Global Reach → Configuring a custom domain in Route 53 and integrating with CloudFront for global content delivery and low-latency user experience.
- Monitoring & Governance → Setting up CloudWatch for observability, IAM for secure access management, and following AWS Well-Architected Framework principles.

This project not only teaches “how to build” but also why these design choices matter — preparing learners to think like AWS Solution Architects.

## Prerequisites

- AWS account with required permissions
- Basic knowledge of HTML/CSS and AWS console
- Optional: AWS CLI installed and configured

---
---
## Step-by-Step Deployment Guide

### 1. VPC & Networking
- Create a new VPC (CIDR: 10.0.0.0/16)
- Create public and private subnets
  - 1 public and 2 private subnets. Distribute them across Availability Zones [AZ]
- Create & Attach Internet Gateway (IGW)
- Create NAT Gateway for private subnet access
- Configure route tables
  - Create public route table and make it to public subnet
  - Create private route table and map it to private subnets

### 2. Security
- Create Security Groups for EC2, RDS, ALB, Lambda
- Create IAM Roles & Policies with least-privilege

### 3. Compute Layer
- Launch EC2 instances in public & private subnets
- Mount EFS and configure EBS as needed
- Install web server (Apache), php, php-mysqli to serve HTML on EC2 in public subnet\
  Commands:
  ```
  sudo dnf update -y
  ```
  ```
  sudo dnf install -y httpd php php-mysqli
  ```
  ```
  sudo systemctl start httpd
  ```
  ```
  sudo systemctl enable httpd
  ```
  Detailed steps provided [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html]

### 4. Load Balancing & Scaling
- Create Application Load Balancer in public subnets
- Attach listeners (HTTP/HTTPS)
- Create Auto Scaling Group with min/max capacity
- Attach EC2 instances to target group

### 5. Data Layer
- Create RDS (MySQL) instance in private subnet\
  + Detailed steps provided [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html]
- Create DynamoDB table
- Connect application layer to databases

### 6. Static Website
- Create S3 bucket for static HTML/CSS/JS
- Upload front-end files
- Configure CloudFront distribution
- Enable HTTPS with ACM certificate

### 7. Serverless Tasks
- Create Lambda function(s) for background tasks
- Connect Lambda to RDS or DynamoDB if needed

### 8. Domain Integration
- Configure Route 53 hosted zone for `awscloudsolution.shop`
- Point domain to CloudFront or ALB
- Ensure HTTPS is enabled

### 9. Monitoring
- Configure CloudWatch logs and metrics
- Create CloudWatch alarms for EC2, RDS, Lambda, and ALB

### 10. Testing
- Visit your domain and verify front-end loads
- Test database connectivity
- Verify Lambda and serverless tasks execute successfully

### 11. Cleanup
- Delete AWS resources manually to avoid charges
- Optional: Keep a reference list of created resources for learners

---

## Sample Front-End (HTML Application)

**File structure:** `app/web/`


# Repository Structure:

### aws-three-tier-project/
```
├── README.md                 <-- Main project overview & quick start
├── docs/
│   ├── architecture.png      <-- Architecture diagram
│   ├── network-diagram.png   <-- Optional detailed VPC/subnet diagram
│   └── README-AWS-STYLE.md   <-- AWS-style documentation guide
├── app/
│   ├── web/                  <-- Front-end HTML/CSS/JS files
│   │   ├── index.html
│   │   ├── SamplePage.php
│   │   └── dbinfo.inc
│   └── worker/               <-- Lambda code or other scripts
│       └── lambda_handler.js
├── scripts/
│   └── deploy.sh             <-- Optional helper script for deployment
└── examples/                 <-- Screenshots or config snippets for reference
```
