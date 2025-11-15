provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "repo" {
  name = "ai-document-intelligence"
}

resource "aws_s3_bucket" "storage" {
  bucket = "ai-documents-storage"
}
