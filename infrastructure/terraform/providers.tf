terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  backend "s3" {
    encrypt = true
    region  = "eu-central-1"
  }

  required_version = ">= 1.4.6"
}

provider "aws" {
  region = "eu-central-1"
  default_tags {
    tags = {
      purpose = "customer-facing"
      product = "api"
    }
  }
}
