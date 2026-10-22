# Feeling-Oriented Product & Interaction Design

Version 1.0 | Project-neutral | Applies from idea to operations.

## Core contract
Design for both task success and the intended human experience. Intended feelings are **design hypotheses**, not facts about users. Validate through appropriately sampled user research, accessibility testing and ongoing feedback. Avoid assumptions about how disability, age, culture or identity determines emotion.

Every material journey must document **User goal -> Intended feeling -> Interaction behavior -> Risk/friction -> Recovery behavior -> Evidence/measurement -> Owner**.

## Experience principles
- **Agency and dignity:** users understand options, consent, escape routes and consequences; do not coerce or shame.
- **Confidence and trust:** predictable behavior, understandable system state, credible feedback; honest limits and uncertainty.
- **Ease and calm:** reduce unnecessary steps, surprises, latency and visual/cognitive load without hiding important details.
- **Belonging and inclusion:** accessible, respectful, culturally aware interactions developed with affected users.
- **Consistency:** typography, controls, visual language, focus, states and copy feel coherent across workflows and platforms.
- **Recovery and resilience:** helpful errors, safe retry, undo when feasible, interruption recovery and clear ownership of next step.
- **Delight with restraint:** never trade clarity, accessibility, safety or performance for decoration or engagement manipulation.
- **Privacy as felt and real safety:** transparent data handling backed by actual technical controls.

## Cross-lifecycle requirements
| Stage | Feeling-oriented deliverable | Gate/evidence |
|---|---|---|
| Idea, discovery | Experience promise, target users, emotional jobs, sensitive contexts | Separate research findings from assumptions |
| Product charter | Desired and undesired experiences, ethical constraints | Human-approved experience principles |
| Capabilities and journeys | Journey maps with intended feelings and risky moments | Coverage of happy, unhappy and recovery paths |
| Requirements | Observable interaction criteria and testable failure/recovery states | Traceability from goal to acceptance criteria |
| Architecture | Latency, reliability, interruption, status and privacy mechanisms | Measurable service and interaction constraints |
| Walking skeleton | Real end-to-end interaction, not only API success | Demonstrated user flow including one failure case |
| Iteration | Consistent components, microcopy, keyboard/screen-reader and input affordances as applicable | Review design and technical implementation together |
| QA and pilot | Moderated usability, accessible research methods, task success, trust/frustration questions | Consent-based research and documented findings |
| Deployment and operations | Status messaging, rollback effects, support and incident communication | Actual experience and operations evidence |
| Evolution | Complaints, qualitative feedback and opt-in sentiment alongside behavior measures | Prioritized, traceable improvements |

## Journey acceptance card template
- Journey ID and user group/context:
- User goal and success criteria:
- Intended feelings (hypotheses, e.g. confident / respected):
- Undesired feelings and likely triggers:
- Preconditions and accessibility needs:
- Interface interactions, feedback, loading and system states:
- Failure, interruption, escape, retry and recovery path:
- Data use, consent, transparency and safety:
- Observable acceptance criteria (including technical thresholds where justified):
- Research method, participant consent and evidence link:
- Result: NOT_TESTED / MIXED / SUPPORTED / NOT_SUPPORTED:
- Owner and next action:

## Validation signals
Triangulate completion and error rates, time-on-task, recoverability, accessibility findings, interviews, voluntary short post-task questions and support trends. Be careful: self-reported feelings are context-dependent; avoid implying causal certainty or optimizing an emotional score at the expense of agency. Record sample limitations and conflicting feedback.

## Example: communication platform (illustrative, not mandatory)
Goal: invite another participant into an ongoing video conversation. Intended feeling: in control. Verify clear consent, visible join/leave status, privacy-friendly defaults and a recoverable connection error. Do not assert users felt empowered without user evidence.

## Review policy
A feature may pass automated tests and still fail the experience gate. Record that separately. High-stakes or accessibility-specific journeys require qualified human review; AI-generated sentiment predictions are not user research.