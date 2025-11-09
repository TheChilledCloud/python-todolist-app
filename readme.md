# Python Todo-List DevOps Project

This is my **first DevOps project** where I'm learning DevOps fundamentals through hands-on practice. I containerized a simple Python todo-list application and set up automated deployment to AWS ECR using modern DevOps tools. I'd really appreciate any feedback or suggestions for improvement!

**What I Implemented:**
- Dockerized a Python todo-list application
- Created a CI/CD pipeline using GitHub Actions
- Used Terraform for Infrastructure as Code
- Deployed to AWS ECR

## 🛠 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Containerization** | Docker, Amazon ECR |
| **Cloud Platform** | AWS ECR |
| **IaC** | Terraform |
| **CI/CD** | GitHub Actions |
| **Programming** | Python |
| **Version Control** | Git, GitHub |

## Features

- **Infrastructure as Code**: Terraform provisions and manages AWS ECR resources
- **Container**: Docker builds the app image
- **CI/CD**: GitHub Actions pipeline automatically creates the registry on AWS (using terraform) and builds the image using Dockerfile, then pushes the image to AWS ECR

## Quick Start

### Prerequisites

- Docker 
- AWS CLI
- Terraform
- Github account
- AWS (for AWS deployment)

#### Local Development

- Clone the repository
```git clone https://github.com/TheChilledCloud/python-todolist-app```
```cd python-todolist-app```

- Build Docker image
```docker build -t python-todo-app -f docker-files/Dockerfile .```

- Run container locally
```docker run -p 5000:5000 python-todo-app```

### Deploy to AWS

Fork the repository, then setup AWS Secret Access key, AWS Access Key ID & AWS Region and save in github secretes and variables
Run the pipeline

## Project Structure
```
.
├── .github/workflows/
│ └── buildAndPush.yml     # CI/CD pipeline
├── terraform/
│ ├── ecr.tf               # Infrastructure definition
│ ├── vars.tf
│ └── provider.tf
│ └── .terraform.lock.hcl
├── docker-files/
│ └── Dockerfile           # Container definition
├── todo_app.py            # Python application
├── requirements.txt
├── .gitignore
└── README.md
```

## CI/CD Pipeline

The GitHub Actions workflow automates the following:
- **Infrastructure**: Terraform provisions/ updates AWS resource ECR
- **Build**: Creates Docker image from application code
- **Push**: Uploads the image ot AWS ECR

## Learning Outcomes

Through this project, I gained hands-on experience with:
- Containerizing applications with Docker
- Building automated CI/CD pipelines with GitHub Actions
- Managing cloud infrastructure with Terraform
- Working with AWS ECR
- Implementing DevOps best practices
- Git version control

## Security Considerations

- AWS credentials managed via GitHub Secrets
- Minimal IAM permissions following least privilege

## Connect

Built as part of my DevOps learning journey. Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/ahmad-alfaisal/)

---

⭐ **Star this repo** if you found it helpful!