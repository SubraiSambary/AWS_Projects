# Repository Structure:

### aws-three-tier-project/
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
