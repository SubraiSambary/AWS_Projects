# Project Overview 

The purpose of this project is to demonstrate how to design and deploy a simple three-tier application architecture on AWS while also showcasing automation using serverless services. The project helps learners:
- Understand core AWS services such as VPC, EC2, S3, CloudFront, RDS, DynamoDB, IAM, and Route 53.
- Learn how to host and serve a static website with HTML and connect it to a backend (PHP page on EC2).
- Explore AWS automation by using Lambda and EventBridge to automatically start an EC2 instance on a schedule.
- Practice implementing networking, security, and monitoring best practices as per AWS Solutions Architect Associate-level knowledge.

# Components 
- ### VPC
- ### EC2
- ### LOAD BALANCING
- ### AUTO SCALING
- ### RDS (MYSQL)
- ### DOMAIN MAPPING
- ### ROUTE53
- ### EFS
- ### S3
- ### IAM
- ### DYNAMODB
- ### LAMBDA
- ### CLOUDFRONT
- ### CLOUDWATCH



## Sample Front-End (HTML Application)

**File structure:** `app/web/`


# Repository Structure:

### aws-three-tier-project/
```
├── README.md                 <-- Main project overview & quick start
├── docs/
│   ├── architecture.png      <-- Architecture diagram
│   ├── network-diagram.png   <-- Optional detailed VPC/subnet diagram
│   └── GUIDE-TO-IMPLEMENT.md   <-- Step by Step Guide
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
