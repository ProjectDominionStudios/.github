# Contributing to Project Dominion Studios

Thank you for helping build Project Dominion Studios.

## Before starting

1. Read the target repository's README and contribution notes.
2. Confirm the work belongs in that repository.
3. Open or reference a GitHub issue with a clear outcome and acceptance criteria.
4. Start from current `main`; do not build new work on an old merged branch.

## Branches

Use short-lived branches:

- `feature/<description>`
- `fix/<description>`
- `docs/<description>`
- `chore/<description>`

## Pull requests

Pull requests should be small enough to review safely and include:

- what changed
- why it changed
- user or contributor impact
- validation performed
- screenshots or visual comparisons for UI and design work
- linked issues and relevant decisions

Keep `main` buildable and do not commit secrets, credentials, personal data, generated caches, or unnecessary binaries.

## Repository boundaries

Do not duplicate authoritative content across repositories. Link to the source of truth instead.

- Game rules belong in `ProjectDominion`.
- Production visual assets belong in `ProjectDominion.Design`.
- Canon belongs in `ProjectDominion.Lore`.
- Deployment definitions belong in `ProjectDominion.Infrastructure`.
- Automation exports belong in `ProjectDominion.n8n`.

## AI-assisted work

AI-generated changes require human review. Verify behavior, licensing, security, accessibility, and factual accuracy before merging.

## Sustainable development

Project Dominion Studios values steady, health-aware progress. Scope should be reduced before quality, safety, or contributor wellbeing are sacrificed.