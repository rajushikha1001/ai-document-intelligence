provider "aws" {
  region = var.region
}

resource "aws_ecr_repository" "ai_repo" {
  name = "${var.project_name}-repo"
}

resource "aws_s3_bucket" "storage" {
  bucket = "${var.project_name}-storage"
  force_destroy = true
}

output "ecr_repository_url" {
  value = aws_ecr_repository.ai_repo.repository_url
}

output "s3_bucket_name" {
  value = aws_s3_bucket.storage.bucket
}
