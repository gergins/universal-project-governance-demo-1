# Universal Project Governance Framework

**Status: DRAFT — template readiness not yet verified.** The GitHub import is incomplete relative to the original local v2.3 package. Do not assume all historical skills, references or evaluations were imported. No CI, connected agent runtime, production deployment, or security certification is claimed.

## Start here
Read [Start Here](docs/START_HERE.md) for creating a new product repository and initializing its manifest safely.

**WHAT:** Discover the idea, users, research, domain, human experience, product capabilities and acceptance criteria.

**HOW:** Choose the simplest verified development and execution approach. When an AI workflow is justified, preserve one accountable coordinator, bounded specialists and independent authorization of side effects. Durability is optional.

## Authoritative guides
- [Agent instructions](AGENTS.md)
- [WHAT / HOW](docs/WHAT_HOW_MODEL.md)
- [Capability catalogue](docs/CAPABILITY_CATALOGUE.md)
- [Executable readiness](docs/EXECUTABLE_READINESS_GATE.md)
- [Coordinator execution contract](docs/COORDINATOR_EXECUTION_CONTRACT.md)
- [Simplicity policy](docs/SIMPLICITY_AND_EVOLUTION.md)
- [Assurance boundaries](docs/ASSURANCE_AND_CERTIFICATION.md)
- [Publication status](docs/TEMPLATE_READINESS_STATUS.md)

Other `docs/` files are supporting references, not additional mandatory layers. No documentation automatically grants permission or creates executable integrations.

## Read-only proof
`python -m unittest discover -s tests -v` exercises the limited local prototype. Local results must be observed separately from GitHub CI. A successful test does not prove production deployment or authorization outside the tested path.

## Never assume readiness
The master manifest leaves integrations and execution unconfigured. Review all action boundaries and provider credentials separately. CI must not be enabled as an enforced gate before action pinning and verification.
