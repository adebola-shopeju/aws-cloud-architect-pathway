# Azure Cloud Governance & Resource Organisation Project

**CloudOps Nigeria — Remote-First Azure Architect Program**
**Learner:** Adebola Shopeju
**Completed:** 23 May 2026
**Program:** 3MTT / Darey.io Cloud Engineering Track

---

## Project Overview

This project demonstrates fundamental Azure cloud governance principles through hands-on implementation in the Azure Portal and Azure CLI. The goal was to design and deploy a scalable, well-governed Azure environment that maintains control over costs, access, and resource lifecycle as cloud environments grow in complexity.

The project covers four pillars of cloud governance:

- **Resource organisation** — grouping related assets using resource groups
- **Naming conventions** — consistent, descriptive names that communicate environment, region, and purpose at a glance
- **Tagging strategy** — metadata attached to every resource for cost allocation and reporting
- **Role-Based Access Control (RBAC)** — restricting team access to only what their role requires

---

## Architecture

### Resource Groups Created

| Resource Group | Environment | Region | Purpose |
|---|---|---|---|
| `rg-cloudops-dev-northeu-001` | Development | North Europe | Development team workspace |
| `rg-cloudops-prod-northeu-001` | Production | North Europe | Live production environment |
| `rg-cloudops-test-northeu-001` | Testing | North Europe | Temporary testing (deleted — lifecycle demo) |

### Resources Deployed

| Resource | Resource Group | Type | Redundancy |
|---|---|---|---|
| `stcloudopsdevnortheu001` | dev | Storage Account | LRS (cost-appropriate for dev) |
| `stcloudopsprodnoreu001` | prod | Storage Account | ZRS (higher protection for production) |

---

## Naming Convention

All resources follow this standard format:

```
[resource-type]-[project]-[environment]-[region]-[number]
```

### Abbreviations Used

| Resource Type | Prefix |
|---|---|
| Resource Group | `rg` |
| Storage Account | `st` |
| Virtual Machine | `vm` |
| Database | `db` |

### Why This Matters

A consistent naming convention means any engineer joining the team can identify a resource's purpose, environment, and region without opening it. `rg-cloudops-prod-northeu-001` communicates project, environment, region, and sequence in a single string — eliminating ambiguity and reducing the risk of accidental modifications to the wrong environment.

---

## Tagging Strategy

Every resource was tagged with three key-value pairs at deployment:

| Tag Key | Dev Value | Prod Value | Purpose |
|---|---|---|---|
| `environment` | `dev` | `prod` | Separate dev and prod costs in billing reports |
| `owner` | `teamA` | `teamA` | Attribute spend to the responsible team |
| `project` | `cloudops` | `cloudops` | Group all project resources for total cost reporting |

### Real-World Impact

Tags enable a finance director to filter Azure Cost Management by any tag and instantly answer:
- *"How much did the dev environment cost this month?"* — filter by `environment=dev`
- *"What did TeamA spend?"* — filter by `owner=teamA`
- *"What is the total project cost?"* — filter by `project=cloudops`

Without tags, these questions are impossible to answer accurately across a large Azure environment.

---

## RBAC — Role-Based Access Control

RBAC was implemented on `rg-cloudops-dev-northeu-001` to simulate a multi-team environment.

### Roles Assigned

| Principal | Role | Scope | Rationale |
|---|---|---|---|
| TeamA (Senior Engineers) | Contributor | dev resource group | Full management access to build and test — cannot assign roles to others |
| TeamB (Junior Interns) | Reader | dev resource group | Read-only visibility — can observe without making changes |
| All teams | No access | prod resource group | Production changes must go through a controlled release process |

### Why Production Has No Team Access

Production environments contain live services and customer data. Even senior engineers do not have direct production access — all changes must be tested in dev, approved, and deployed through a controlled process. This principle of **least privilege** ensures that accidental modifications, misconfigurations, or deletions cannot directly impact customers.

### How RBAC Was Implemented

Due to an Azure Portal UI issue, roles were assigned using the Azure CLI — which is the preferred method in professional environments for repeatability and auditability:

```bash
# Assign Contributor role to TeamA (Senior Engineers)
az role assignment create \
  --assignee-object-id "1e19d968-81a3-4251-bb0d-7bf4527cc1ee" \
  --assignee-principal-type User \
  --role "Contributor" \
  --scope "/subscriptions/9f7b244f-8563-41e8-b3c6-0df0f515b741/resourceGroups/rg-cloudops-dev-northeu-001"

# Assign Reader role to TeamB (Junior Interns)
az role assignment create \
  --assignee-object-id "1e19d968-81a3-4251-bb0d-7bf4527cc1ee" \
  --assignee-principal-type User \
  --role "Reader" \
  --scope "/subscriptions/9f7b244f-8563-41e8-b3c6-0df0f515b741/resourceGroups/rg-cloudops-dev-northeu-001"

# Verify all role assignments
az role assignment list \
  --resource-group "rg-cloudops-dev-northeu-001" \
  --output table
```

---

## Resource Lifecycle Management

The test resource group (`rg-cloudops-test-northeu-001`) was created and subsequently deleted to demonstrate lifecycle management — one of the most cost-critical skills in cloud governance.

Deleting a resource group removes all contained resources in a single operation, preventing unnecessary cost accumulation from abandoned environments. In professional Azure environments, temporary environments that are not cleaned up are a major source of unexpected cloud spend.

```bash
# Delete the test resource group and all its contents
az group delete --name "rg-cloudops-test-northeu-001" --yes

# Verify deletion
az group list --output table
```

---

## Azure CLI Commands Reference

All commands used in this project:

```bash
# Login to Azure
az login

# List all resource groups
az group list --output table

# Delete a resource group
az group delete --name "rg-cloudops-test-northeu-001" --yes

# Get current user Object ID
az ad signed-in-user show --query id -o tsv

# Assign Contributor role
az role assignment create \
  --assignee-object-id "1e19d968-81a3-4251-bb0d-7bf4527cc1ee" \
  --assignee-principal-type User \
  --role "Contributor" \
  --scope "/subscriptions/9f7b244f-8563-41e8-b3c6-0df0f515b741/resourceGroups/rg-cloudops-dev-northeu-001"

# Assign Reader role
az role assignment create \
  --assignee-object-id "1e19d968-81a3-4251-bb0d-7bf4527cc1ee" \
  --assignee-principal-type User \
  --role "Reader" \
  --scope "/subscriptions/9f7b244f-8563-41e8-b3c6-0df0f515b741/resourceGroups/rg-cloudops-dev-northeu-001"

# List role assignments
az role assignment list \
  --resource-group "rg-cloudops-dev-northeu-001" \
  --output table
```

---

## Screenshots

All screenshots are located in the `/screenshots` folder of this repository:

| File | Contents |
|---|---|
| `01_dev_resource_group.png` | rg-cloudops-dev-northeu-001 created |
| `02_prod_resource_group.png` | rg-cloudops-prod-northeu-001 created |
| `03_test_resource_group.png` | rg-cloudops-test-northeu-001 created |
| `04_all_resource_groups.png` | All three resource groups in list view |
| `05_dev_storage_account.png` | stcloudopsdevnortheu001 deployed with tags |
| `06_prod_storage_deployed.png` | stcloudopsprodnoreu001 deployment success |
| `07_rbac_cli_contributor.png` | Contributor role assigned via CLI |
| `08_rbac_cli_reader.png` | Reader role assigned via CLI |
| `09_rbac_verification.png` | Role assignment list confirming both roles |
| `10_test_group_deleted.png` | az group list confirming test group removed |

---

## Key Learnings

1. **Tags are not access controls** — tags track cost and ownership; RBAC controls access. These are separate tools with separate purposes.
2. **Redundancy reflects environment** — dev uses LRS (cheap, acceptable risk); prod uses ZRS (higher protection, justified cost).
3. **CLI over portal for reliability** — the Azure Portal can have UI issues; the CLI always works and produces auditable, repeatable commands.
4. **Lifecycle management prevents bill shock** — deleting unused environments is as important as creating them.
5. **Least privilege protects production** — nobody gets more access than their role requires.

---

*CloudOps Nigeria · Remote-First Azure Architect Program · Week 1 Project*
