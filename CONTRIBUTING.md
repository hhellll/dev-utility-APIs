# Contributing

Thanks for your interest in improving these APIs. Contributions of all kinds are welcome: bug reports, documentation improvements, and code changes.

## Ground rules

- All discussion, issues, pull requests, and documentation are in English.
- Never commit secrets, API keys, tokens, or `.env` files.
- Keep each pull request focused on a single change. Small, reviewable PRs merge faster than large ones.

## Workflow

1. Fork the repository (or, if you have write access, work directly in it).
2. Create a branch from `main` with a descriptive name, for example `fix/email-validator-timeout` or `docs/readme-refresh`.
3. Make your change. If you change an API's behavior, update its documentation and the changelog in the same pull request.
4. Open a pull request against `main` and describe what changed and why. Link any related issue.
5. Wait for review. Direct commits to `main` are not accepted; every change lands through a pull request.

## Reporting bugs

Open an issue using the bug report template and include steps to reproduce, the expected behavior, and the actual behavior. For security vulnerabilities, do not open a public issue — follow [SECURITY.md](SECURITY.md) instead.

## Code style

- Python code follows the existing style of the API you are touching.
- Keep functions small and typed where practical.
- Do not add dependencies without explaining why in the pull request.
