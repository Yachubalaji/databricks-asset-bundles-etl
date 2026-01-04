variable "databricks_host" {
  description = "Databricks workspace host, e.g. https://adb-xxxx.azuredatabricks.net"
  type        = string
}

variable "databricks_token" {
  description = "Databricks personal access token (PAT). Consider using environment variables or a secrets manager."
  type        = string
  sensitive   = true
}
