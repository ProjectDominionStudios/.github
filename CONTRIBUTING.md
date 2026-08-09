# Contributing to Project Dominion Studios

Status: **Published organization default**

Knowledge Object ID: `PDS-KO-PUB-GITHUB-CONTRIBUTING-0001`

Thank you for helping build Project Dominion Studios.

## Before starting

1. Read the target repository's README, governance, security, and contribution
   notes.
2. Confirm the work belongs in that repository and identify the canonical owner
   of any knowledge being changed.
3. Open or reference one GitHub issue with a bounded outcome, acceptance
   criteria, validation, and rollback approach.
4. Start from current `main` and confirm the baseline is clean.

## Development workflow

- Use one issue, one short-lived branch, and one pull request per implementation
  unit.
- Use `issue-<number>-<short-description>` for a general branch. Codex-created
  branches use `agent/issue-<number>-<short-scope>`.
- Keep commits focused and descriptive.
- Preserve provenance and Git history when moving canonical knowledge.
- Validate before merge; merge only after required checks pass.
- Delete the completed branch after merge and verify the linked issue closed.

## Pull requests

Explain what changed, why it belongs in the repository, affected knowledge
ownership, risk, validation, rollback, and any human/machine documentation
updates. Include screenshots or accessible previews when visual behavior
changes.

## Public and sensitive information

Do not commit credentials, tokens, keys, recovery material, personal data,
private operational details, generated caches, or unnecessary binaries.
Public placement does not itself authorize publication. Follow the stricter
repository-specific classification, privacy, security, and approval rules.

## AI-assisted work

AI may assist with analysis and implementation, but it does not approve its own
authority. A human remains accountable for correctness, licensing, security,
privacy, accessibility, and external effects.

Repository-specific requirements take precedence over these organization
defaults.
