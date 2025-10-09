# Project Overview 

The purpose of this project is to demonstrate how to design and deploy a simple three-tier application architecture on AWS while also showcasing automation using serverless services. The project helps learners:
- Understand core AWS services such as VPC, EC2, S3, CloudFront, RDS, DynamoDB, IAM, and Route 53.
- Learn how to host and serve a static website with HTML and connect it to a backend (PHP page on EC2).
- Explore AWS automation by using Lambda and EventBridge to automatically start an EC2 instance on a schedule.
- Practice implementing networking, security, and monitoring best practices as per AWS Solutions Architect Associate-level knowledge.

# Architecture
![architecture](https://github.com/SubraiSambary/AWS_Projects/blob/main/aws-three-tier-project/docs/three-tier-architecture.png)

# Components 
- ### VPC (Virtual Private Cloud)
  A logically isolated network within AWS where you can launch resources securely. It allows control over IP ranges, subnets, routing, and security.
- ### EC2 (Elastic Compute Cloud)
  Scalable virtual servers for running applications. Provides flexible compute capacity with various instance types and configurations.
- ### LOAD BALANCING
  Distributes incoming traffic across multiple EC2 instances to ensure high availability and fault tolerance.
- ### AUTO SCALING
  Automatically adjusts the number of EC2 instances based on traffic or performance metrics to maintain application availability and optimize costs.
  By defalut the desired instances would be set to 0. This scaling would be then controlled via EventBridge schedules to start and stop the EC2 instances.
- ### RDS (MYSQL)
  Managed relational database service that simplifies setup, operation, and scaling of MySQL databases with automated backups and patching.
- ### DOMAIN MAPPING
  Associates your custom domain name with AWS resources (like EC2 or Load Balancer) for user-friendly access.
- ### ROUTE53
  Highly available DNS service for domain registration, routing traffic, and health checks of resources.
- ### EFS
  Scalable, shared file storage for EC2 instances, ideal for applications requiring distributed access to files.
- ### S3
  Object storage for storing and retrieving any amount of data, commonly used for backups, static content, and media files.
  S3 mounting is not officially supported by AWS. However, it can be used to store files, images which would be displayed on the website.
  Note: Mounting can also be tried if interested.
- ### IAM
  Controls access to AWS services and resources securely using users, roles, and policies.
  IAM roles and policies need to be attached to components such as Lambda, EC2 to enable them to connect with other required AWS components such as ASG and S3.
- ### LAMBDA
  Serverless compute service that runs code in response to events without provisioning or managing servers.
  Start and Stop EC2 instance python scripts are configured in 2 different lambda functions. Each function is called based on 2 seperate schedules in EventBridge.
- ### CLOUDFRONT
  Content Delivery Network (CDN) that caches and delivers content globally with low latency and high transfer speeds.
- ### EVENTBRIDGE
  A serverless service that uses events to connect application components together, making it easier for developers to build scalable event-driven applications.
  2 Schedules need to be configured, one which runs at a specified time with cron to start EC2 instances and one which runs at a specified time with cron to stop EC2 instances.


## Sample Front-End (HTML Application)

**File structure:** `app/web/`


# Repository Structure:

### aws-three-tier-project/
```
├── README.md                 <-- Main project overview & quick start
├── docs/
│   ├── architecture.png      <-- Architecture diagram
│   └── network-diagram.png   <-- Optional detailed VPC/subnet diagram
├── app/
│   ├── web/                  <-- Front-end HTML/CSS/JS files
│   │   ├── index.html
│   │   ├── SamplePage.php
│   │   └── dbinfo.inc
│   └── worker/               <-- Lambda code or other scripts
├── scripts/
│   └── startEC2_Lambda.py    <-- Lambda code to change ASG desired capacity to 2
│   └── stopEC2_Lambda.py     <-- Lambda code to change ASG desired capacity to 0
│   └── IAMRolePolicy_JSON    <-- JSON Policy for the role to be attached to lambda
└── examples/                 <-- Screenshots or config snippets for reference
```
