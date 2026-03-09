terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
    credentials = "./credetials/keys.json"
  project = "zoomcamp-489722"
  region = "us-central1"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "zoomcamp-489722-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}