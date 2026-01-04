# Databricks Asset Bundle – Serverless ETL Demo

This project demonstrates how to use **Databricks Asset Bundles (DAB)** to deploy and run a production-style ETL job using **serverless compute**.

The goal is to showcase how Databricks Asset Bundles enable:
- Infrastructure-as-code style job definitions
- Environment-aware deployments (dev / prod)
- Reproducible, version-controlled Databricks workflows

---

## What this project does

- Downloads the Iris dataset from a public source
- Performs a simple aggregation (count by species)
- Writes results to a Delta table in Databricks
- Runs fully on **Databricks Serverless Jobs**

---

## Key Technologies

- Databricks Asset Bundles
- Databricks Serverless Jobs
- PySpark
- Delta Lake
- Git-based deployment workflow

---

## Why Asset Bundles?

Asset Bundles allow Databricks jobs to be:
- Defined declaratively (YAML)
- Version-controlled
- Deployed consistently across environments
- Managed without manual UI configuration

This aligns closely with modern data platform and DevOps best practices.

---

## How to run

```bash
databricks bundle validate
databricks bundle deploy -t dev
databricks bundle run simple_iris_etl -t dev
