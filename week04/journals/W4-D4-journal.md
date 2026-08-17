## Week 4 Day 4 — Secrets Manager & Parameter Store

| | Secrets Manager | Parameter Store |
|---|---|---|
| Use case | Passwords, API keys, credentials that need protecting | App config, env flags, non-sensitive settings |
| Cost | $0.40/month per secret | Free (Standard tier) |
| Rotation | Supports automatic rotation (via Lambda) | No built in rotation |
| Encryption | Always encrypted (KMS) | Only SecureString type is encrypted |

**Real error hit today:** `adebola_dev` got `AccessDeniedException` trying to create a secret  had to have `SecretsManagerReadWrite` attached via root. Lesson: every AWS API call is a permission check first.

