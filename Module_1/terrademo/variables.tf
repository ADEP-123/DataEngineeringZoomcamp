variable "credentials" {
  description = "Path to the GCP credentials file."
  default     = "./credetials/keys.json"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "region" {
  description = "Project region"
  default     = "us-central1"
}

variable "project" {
  description = "Project ID"
  default     = "zoomcamp-489722"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name."
  type        = string
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name."
  default     = "zoomcamp-489722-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}