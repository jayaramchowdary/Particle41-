# SimpleTimeService
This repo includes a minimal Flask web service that returns the current timestamp and client IP. It is containerized with Docker and deployed to AWS ECS Fargate using Terraform.

## Prerequisites
- Docker: https://docs.docker.com/get-docker/
- AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
- Terraform: https://developer.hashicorp.com/terraform/downloads

## Docker Instructions
```
docker build -t simple-time-service ./app
docker run -p 8080:80 simple-time-service
```
Visit `http://localhost:8080` in browser or curl it.

## Terraform Deployment
1. Configure AWS CLI with credentials:
   ```bash
   aws configure
   ```
2. Navigate to terraform folder:
   ```bash
   cd terraform
   terraform init
   terraform apply -var-file="terraform.tfvars"
   ```

After deployment, Terraform will output the Load Balancer DNS to access the app.

## Notes
- The container runs as a non-root user.
- Infrastructure follows Terraform and AWS best practices.
- Clean up after testing to avoid AWS charges:
  ```bash
  terraform destroy -var-file="terraform.tfvars"
