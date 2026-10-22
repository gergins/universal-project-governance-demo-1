# OpenAI documentation alignment (reviewed 2026-10-22)

OpenAI has **not endorsed or certified** this framework. The following are aligned design choices rather than certification claims:

- Keep `AGENTS.md` short, point at relevant docs instead of mandating full-context reads: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Use optional repo instructions and task-specific workflow artifacts: https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex
- Use small skills with `SKILL.md` metadata for repeatable focused work: https://developers.openai.com/plugins/concepts/skills
- Authorize high-risk tool actions at the runtime boundary; HITL approval is not replaced by a prompt: https://openai.github.io/openai-agents-python/human_in_the_loop/
- Evaluate orchestration with deterministic tests where possible and use real integrations for external behavior: https://openai.github.io/openai-agents-python/testing/
- Tracing can assist debugging, but sensitive content handling and retention require attention: https://openai.github.io/openai-agents-python/tracing/

Our choices, **not** OpenAI requirements: the 18-stage lifecycle, feeling-oriented design rubric, status vocabulary, repository manifest and chosen gate matrix.