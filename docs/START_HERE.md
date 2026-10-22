# Start here — universal idea to product

The user-facing distinction is **WHAT** (idea, research, domain, human experience, capabilities) and **HOW** (the simplest controlled approach to build, verify and operate).

## New project
1. First, finish master-template readiness checks; do not assume this repository is ready simply because files are present.
2. Create a **copy** of the master template, never initialize the master in place.
3. Record the actual source commit: `git rev-parse HEAD` in master. In the copy, run `python scripts/initialize_project.py --name "PROJECT" --repository "OWNER/PROJECT" --owner "OWNER" --description "PURPOSE" --source-sha "40_HEX_SOURCE_SHA"`.
4. Run `python scripts/validate_framework.py` and `python -m unittest discover -s tests -v` locally. They do not prove external API access or release readiness.
5. In the project, define a short idea brief and select only relevant capability domains from `docs/CAPABILITY_CATALOGUE.md`.
6. Use `AGENTS.md` for operating boundaries and refer to specific supporting documents only when needed.
7. Before external actions, verify real adapters, authorization, concrete approvals, evidence and recovery. No credentials or integrations are supplied by this template.

## Stable invariants
One accountable coordinator, bounded specialists, independently enforced action permissions, verifiable outcomes, optional durability when justified. Preserve these without adding needless agents or layers.

## Source-of-truth references
- WHAT/HOW: `docs/WHAT_HOW_MODEL.md`
- Executable actions: `docs/EXECUTABLE_READINESS_GATE.md`
- Agent coordination: `docs/COORDINATOR_EXECUTION_CONTRACT.md`
- Assurance: `docs/ASSURANCE_AND_CERTIFICATION.md`
- Publication readiness: `docs/TEMPLATE_READINESS_STATUS.md`

Other documents are supporting detail and historical design references.
