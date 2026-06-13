# Security Policy

This repository is intended to contain reusable skill logic, not credentials.

If you find a committed secret:

1. Remove it immediately.
2. Rotate the credential with the provider.
3. Rewrite repository history if the secret was pushed.
4. Add a validation rule to prevent recurrence.

Use environment variables or local untracked config files for all tokens.
