# Simplicity and Evolution Policy

## Prime directive
Prefer the simplest architecture that meets verified product goals, required controls, and failure-recovery needs. Simplicity must never be achieved by removing essential authorization, independent verification, accessibility, or safety.

## Always-on optimization review
For every proposed idea, feature, agent, module, workflow, or rule, ask:
1. Does an approved capability already solve this? Reuse before building.
2. Can the same result be obtained with deterministic code, a human workflow, or one agent? Start there.
3. Does a new abstraction have a clear, unique responsibility, measurable benefit and owner? If not, do not create it.
4. Is this requirement actually relevant to this project? Selectively activate it; avoid maximal boilerplate.
5. What failure or risk would the change introduce? Retain controls at execution boundaries.
6. Can we replace duplication with one canonical contract and a short reference?
7. How will we compare before/after: steps, code, maintenance, latency, cost, errors, verification quality and human experience?
8. What does the user need to know now, rather than every conceivable future detail? Surface only material prerequisites.

## Complexity escalation ladder
Use deterministic rules or direct functions first; then single model call; then one tool-using agent; then one accountable manager with bounded specialists if necessary; then durable workflow engines if interruption and recovery needs warrant them. This is a selection guide, not a mandatory sequence or proof of implementation.

## Change control
Document consequential choices as a brief ADR with alternatives, evidence, tradeoffs, resulting complexity, reversible migration and a trigger to revisit. Do not create a new specialist, framework integration, or policy document solely for a hypothetical feature. Consolidate older redundant instructions before adding new ones. Project owners choose scope and approve consequential changes.

## Do not confuse philosophy with certification
Aligned with OpenAI's public guidance on small composable primitives and single-agent-first architecture; OpenAI has not reviewed or endorsed this framework.

## Sources (checked October 22, 2026)
- https://openai.github.io/openai-agents-python/
- https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra