<!-- Thank you for contributing! Before you open a PR, please confirm the
checklist below. CI will re-run validate_data.py and linkcheck.py for you;
the human-eye items at the bottom are the ones the curator cares about. -->

## What this PR does

<!-- One short paragraph: which node(s) are touched, what resource(s)
are added/changed/removed, and (for added resources) *why this one*. -->

## Checklist

- [ ] `python tools/validate_data.py` passes locally
- [ ] `python tools/linkcheck.py --only-changed` passes locally
- [ ] Every new resource has an `annotation` ("why this one" in ≤25 words)
- [ ] Every new resource has `addedAt` and `verifiedAt` (both ISO `YYYY-MM-DD`)
- [ ] Every new resource has a `type`, `difficulty`, and `free` flag
- [ ] No node exceeds the **8-resource cap**
- [ ] CHANGELOG.md updated under `## Unreleased`

## Curatorial check (for the reviewer)

<!-- Help the curator review. Optional but appreciated. -->

- Why is this resource a better pick than what's already on the node?
- What did you displace, if anything? Or why did the node have headroom?
- Have you verified the link, title, author, and year yourself?
