# Project Overview

- Purpose of the project

- AWS services used (EC2, RDS, S3, CloudFront, Route 53, Lambda, VPC, etc.)

- Logical architecture diagram placeholder

## Learning Objectives

- What a learner will understand after completing this project

  - e.g., How to set up VPC/subnets, deploy EC2 with Auto Scaling, configure RDS, host a static site on S3 + CloudFront, etc.

## Prerequisites

- AWS account with required permissions
- Basic knowledge of HTML/CSS and AWS console
- Optional: AWS CLI installed and configured

---

# Step-by-Step Deployment Guide

### 1. VPC & Networking
- Create a new VPC (CIDR: 10.0.0.0/16)
- Create public and private subnets
- Attach Internet Gateway (IGW)
- Create NAT Gateway for private subnet access
- Configure route tables

### 2. Security
- Create Security Groups for EC2, RDS, ALB, Lambda
- Create IAM Roles & Policies with least-privilege

### 3. Compute Layer
- Launch EC2 instances in private subnets
- Mount EFS and configure EBS as needed
- Install web server (Apache/Nginx) to serve HTML

### 4. Load Balancing & Scaling
- Create Application Load Balancer in public subnets
- Attach listeners (HTTP/HTTPS)
- Create Auto Scaling Group with min/max capacity
- Attach EC2 instances to target group

### 5. Data Layer
- Create RDS (MySQL) instance in private subnet
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
├── README.md                 <-- Main project overview & quick start\
├── docs/\
│   ├── architecture.png      <-- Architecture diagram\
│   ├── network-diagram.png   <-- Optional detailed VPC/subnet diagram\
│   └── README-AWS-STYLE.md   <-- AWS-style documentation guide\
├── app/\
│   ├── web/                  <-- Front-end HTML/CSS/JS files\
│   │   ├── index.html\
│   │   ├── style.css\
│   │   └── script.js\
│   └── worker/               <-- Lambda code or other scripts\
│       └── lambda_handler.js\
├── scripts/\
│   └── deploy.sh             <-- Optional helper script for deployment\
└── examples/                 <-- Screenshots or config snippets for reference\
```
