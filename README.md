# Databricks Asset Bundles + Terraform (Demo Project)

A small, end-to-end demo showing a **clean split** between:

- **Databricks Asset Bundles** → *job/workflow definition + environment targets*
- **Terraform** → *workspace-level resources (optional), provider wiring, and reproducible infra patterns*

The demo job pulls a **public CSV from the internet** (Iris dataset), performs a tiny transformation, and writes **Delta outputs**.

## What this demo does

- Downloads/reads the Iris dataset CSV from a public URL
- Computes a simple aggregation: **count of rows per species**
- Writes outputs:
  - a managed table: `default.bundle_demo_iris_species_counts`
  - a Delta path: `/tmp/bundle-demo/${env}/iris_species_counts`

## Dataset used
- Iris CSV: `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv`

## Important (data overwrite warning)
⚠️ The job writes with **mode("overwrite")** to keep the demo repeatable.  
It will overwrite:
- table `default.bundle_demo_iris_species_counts`
- Delta path `/tmp/bundle-demo/<env>/iris_species_counts`

If you reuse this in a shared workspace, change the database/path/table names.

---

## Repo structure

```
databricks-asset-bundle-terraform-demo/
├── databricks/
│   ├── databricks.yml
│   └── src/
│       └── iris_etl.py
├── terraform/
│   ├── main.tf
│   ├── providers.tf
│   └── variables.tf
└── .github/workflows/
    └── deploy.yml
```

---

## Prereqs

- A Databricks workspace
- Databricks CLI v0.2+ (or the modern CLI that supports `databricks bundle ...`)
- Auth via one of:
  - `DATABRICKS_HOST` + `DATABRICKS_TOKEN` env vars, or
  - a configured Databricks CLI profile

---

## Deploy & run (local terminal)

From the `databricks/` folder:

```bash
cd databricks

# Validate bundle
databricks bundle validate

# Deploy to dev
databricks bundle deploy -t dev

# Run the job in dev
databricks bundle run simple_iris_etl -t dev

# Deploy/run to prod (same code, different target/root)
databricks bundle deploy -t prod
databricks bundle run simple_iris_etl -t prod
```

---

## Expected output (demo)

The Iris dataset has 150 rows, typically **50 per species**.
Your result table should look like:

| species     | cnt |
|------------|-----|
| setosa     | 50  |
| versicolor | 50  |
| virginica  | 50  |

---

## Terraform (optional)

Terraform is provided as a minimal scaffold. In real projects, you’d often use Terraform for:
- Workspace config / permissions
- Service principals, groups, cluster policies
- Storage, secret scopes, etc.

This demo intentionally keeps Terraform lightweight so the focus stays on **Asset Bundles**.

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

> Note: This scaffold does not create jobs—jobs are managed by the asset bundle.

---

## LinkedIn post idea

> Built a small demo to explore **Databricks Asset Bundles + Terraform**.
> Clean separation: Terraform for infra patterns, Bundles for job deployment.
> Same job, multiple environments, no duplication.
> Repo: <link>

