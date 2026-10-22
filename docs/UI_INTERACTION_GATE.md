# UI interaction and walking-skeleton verification

This is a focused extension of `FEELING_ORIENTED_DESIGN.md` and `RELEASE_GATES.md`, not another governance layer.

## Before writing a screen

For every visible interactive element, capture an entry in a project's `ui-interactions.json` (example: `examples/ui-interactions.example.json`) with these required fields:

- `id`: stable unique identifier
- `surface`: view or component where the control appears
- `trigger`: user action, including keyboard equivalent where appropriate
- `result`: observable expected response, destination, or state
- `data_effect`: what changes in shared data; `none` for read-only
- `persistence`: what survives navigation/reload; `none` when not applicable
- `failure_recovery`: rejection, cancel, unavailable, or error behavior
- `test_ref`: specific planned automated or manual test identifier

A visible control with no intended action should be explicitly non-interactive. Do not simulate functional links or buttons.

## End-to-end acceptance example

Calendar task title → click or keyboard activate → load correct task by ID → open centered task-details dialog → modify priority → save → verify list and calendar show consistent values → reload → verify saved value. Check Escape/cancel and storage failure separately.

A single shared edit action should serve different views. Do not duplicate task editing logic in every screen.

## Deterministic gate

Run `python scripts/validate_ui_contract.py PATH_TO_JSON` on project-specific contracts. It validates completeness and uniqueness of declarations, **not** whether the actual UI works.

A real browser test must exercise representative DOM interactions, including pointer and keyboard paths, navigation, persistence across refresh and a failure/recovery path. Screenshot comparisons or manual visual review check position/responsiveness. A passing unit test is not browser evidence; a render snapshot is not a functioning interaction.

Keep evidence explicit:

- `CONTRACT_PASS`: complete declared interaction schema (not executable validation)
- `UNIT_PASS`: logic tests executed
- `BROWSER_PASS`: real browser interaction observed, with run environment and artifact
- `VISUAL_PASS`: actual rendered layout reviewed against acceptance criteria
- `HUMAN_ACCEPTED`: named human user reviewed subjective expectations
- `BLOCKED`, `FAIL`, `NOT_TESTED`: no success claim

No phase automatically inherits another phase's PASS. When the browser runner is unavailable, record BLOCKED and proceed only if the remaining risk is explicitly accepted; don't substitute speculative claims.

## Agent SDK connection, only when AI is involved

Start with a single coordinator. Add delegated review only for demonstrable benefit. Tracing describes the agent run but is not proof of browser UX. Tool/handoff guardrails do not replace independent authorization, and handoffs must not expand permissions. Prefer existing tools and deterministic tests over creating an agent to click every UI element.

References: OpenAI Agents SDK (https://openai.github.io/openai-agents-python/), OpenAI practical agents guide (https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/), and OpenAI Agents API overview (https://developers.openai.com/api/docs/guides/agents).

## Reusable implementation sequence (each new UI slice)

1. **Inventory:** enumerate visible controls on the affected views. Mark each as actionable or intentionally static, including keyboard operation and empty/error states.
2. **Contract:** record the action, expected target record, shared data effect, persistence and recovery in `ui-interactions.json`. Validate before implementation.
3. **Reuse:** centralize shared actions (for example `openTask(taskId)`); avoid independent editors and persistence logic per view.
4. **Implement one vertical journey:** user trigger → view/controller → real data → save → other view → reload.
5. **Verify separately:** logic tests, real-browser interaction tests, screen layout evidence, and human acceptance. Fix only observed failures.
6. **Report:** attach exact commit, environment, commands, pass/fail counts, browser artifact path and open gaps. A ZIP distribution is not itself a verified release.

**Timebox discovery:** a short review before coding, proportional to risk; do not let completeness analysis block a working small slice indefinitely.

## Interaction coverage and visual acceptance

Review all newly added or touched: navigation items, task/project cards, dates, buttons, row actions, forms, dialogs, filters, lists, empty states and errors. A visual task card is not complete merely because it renders. Its interaction must select the correct entity. Screenshots need to represent the actual running implementation, never unrelated design references.

Use `examples/browser-task-journey.spec.example.ts` as a *porting example* for an app that already uses Playwright. Adapt its accessibility selectors to the actual application, and supply an application-specific running server. This framework does not install browsers, enable CI or claim those example tests were executed.

## Evidence record (per slice)

| Field | Required value |
|---|---|
| Source identity | repository, branch, commit SHA |
| Scope | affected pages and interactions |
| Contract | validator command and result |
| Logic tests | command, counts, outcome |
| Browser interaction | browser, app URL/environment, command, result, trace/screenshot path |
| Visual acceptance | viewport(s), real screenshot review and findings |
| User acceptance | accepted / corrections requested / not tested |
| Open risks | precise failures, blockers and next owner |

No status is inferred from another gate. A browser runner that cannot start is **BLOCKED**, not **PASS**. Only merge or release according to the existing risk-adaptive gates.
