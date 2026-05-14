# Security & abuse reporting

This repo is a curated knowledge artifact, not a software service.
The "vulnerabilities" it can have are different from a typical code
project. This doc explains what we treat as a security/abuse issue
and how to report one.

## What counts as a security issue here

| Category | Examples | How to report |
|---|---|---|
| **Malicious URL** in a curated resource | A resource link that now redirects to malware, phishing, credential-harvesting, or otherwise hostile content. | **Private** — see below. |
| **Doxxing or harassment** introduced via a PR | A PR that injects personal information about a third party, slur content, or harassment language into descriptions / annotations / commit messages. | **Private** — see below. |
| **Supply-chain attack on the renderer** | A PR to `site/` that introduces malicious dependencies, exfiltrating telemetry, or wallet-draining scripts. | **Private** — see below. |
| **Spam, drive-by promotion, or undisclosed conflict of interest** in a resource pick | A PR that adds the contributor's own paid product without disclosure. | A public issue with the `spam` label is fine; severity is low. |
| **Broken link** | A resource that 404s. | Open a normal [`fix-resource` issue](.github/ISSUE_TEMPLATE/fix-resource.yml). Not a security issue. |
| **Disagreement with a curatorial pick** | A resource you think is wrong. | Open the [`Challenge a pick` issue](.github/ISSUE_TEMPLATE/challenge-pick.yml). Not a security issue. |

## How to report (private)

Email **the curator** directly with the details:

- **dongxin DOT guo AT cs.hku.hk** (academic address), or
- via the [GitHub private vulnerability reporting flow](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
  on this repo.

Please include:

1. **What** — the URL, the file, or the PR / commit you're flagging.
2. **Why** — why you believe it's malicious or abusive.
3. **Severity, in your view** — best guess, no formal scoring needed.
4. **Disclosure timeline** — when, if ever, you'd like this made
   public.

You should expect an acknowledgment within **72 hours** during normal
operation (the curator is a full-time PhD candidate; allow longer
during conference season or visa-related travel).

## How we respond

| Severity | Target turnaround |
|---|---|
| Malicious URL in published resource | Same-day removal; fix-up PR; public note in the next monthly pulse. |
| Doxxing / harassment content | Same-day removal; PR-level revert; full git history rewrite if necessary. |
| Supply-chain attack on renderer | Within 24 hours: pin / revert / re-audit dependencies, deploy a re-rendered site, public advisory via [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories). |
| Spam / promotional PR | Within a week: close, leave a public comment with the rationale. |

## Public disclosure norms

- **Coordinated by default.** We will not publicly discuss a reported
  malicious-URL or supply-chain finding until it's been removed.
- **Credit by default.** Reporters who want public credit get it in
  the monthly pulse and in `CHANGELOG.md`.
- **No bug bounty.** This is a personal-academic open-source repo.
  A thank-you and credit is what we can offer.

## Out of scope

The following are not security issues for this repo:

- **Vulnerabilities in resources the roadmap links to.** If a paper's
  arxiv mirror has a flaw, that's arxiv's problem. We will however
  swap the link for a more stable mirror.
- **Vulnerabilities in tools the roadmap recommends.** If vLLM,
  Aider, or any other recommended project has a CVE, file with them.
  We'll note it in a monthly pulse if it changes our recommendation.
- **Disagreement with curatorial choices.** Use the [`Challenge a
  pick`](.github/ISSUE_TEMPLATE/challenge-pick.yml) channel. Strong
  disagreement is welcome; reframing it as "security" is not.

## A note on URL rot

We treat **malicious URL replacement** as a security issue because
content at a stable URL is a trust contract. We treat **404 rot** as
ordinary maintenance: the weekly `linkcheck.yml` cron catches it and
opens a tracking issue. The two failure modes are different in kind
even when they look similar from the outside.
