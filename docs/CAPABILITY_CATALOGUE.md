# Optional capability menu — selecting the WHAT

A domain below is a discovery lens, NOT a mandate to build a corresponding agent, module or artifact.

| ID | Lens | Discover | Typical evidence |
|---|---|---|---|
| IDEA | Idea and strategy | problem, value, goals, positioning, alternatives | brief, success criteria |
| RESEARCH | Research intelligence | existing solutions, research quality, technical feasibility, uncertainty | source register |
| DOMAIN | Domain intelligence | actors, terms, rules, standards, workflows, regulatory boundaries | domain map and expert review |
| HUMAN | Experience and feeling | target emotions, autonomy, friction, accessibility, dignity, trust, recovery | journeys, user research |
| PRODUCT | Product capabilities | jobs, user stories, feature priority, outcomes | requirement IDs, acceptance |
| DESIGN | UX and interaction | flows, IA, visual system, responsive behavior | prototypes and review |
| DATA | Data and knowledge | data types, source, ownership, retention, lineage | schemas/data contract |
| ENGINEER | Engineering | architecture, performance, interoperability, maintenance | ADRs and specs |
| EXECUTE | Executable integrations | registered adapters, tools, scope, auth and outcomes | tool contracts, receipts |
| AGENT | AI and coordination | model vs code, coordinator, specialists, uncertainty | agent rationale and eval plan |
| SECURITY | Security/privacy/safety | trust boundary, abuse cases, permissions, compliance review | threat model and signoffs |
| QUALITY | Testing and assurance | test pyramid, nonfunctional tests, UAT, evals | runnable tests and reports |
| DELIVERY | Delivery and release | infrastructure, CI/CD, deploy, restore, operations | release/rollback plan |
| OPERATE | Operations and evolution | observability, incident response, cost, user feedback | telemetry and backlog |

Selection questions:
1. What outcome is sought? Which lenses materially affect it?
2. Which capabilities already exist and can be reused?
3. Which lens is out of scope, not applicable, or unresolved?
4. Which decision needs human ownership or specialist advice?
5. How will selected capabilities be independently verified?

Every selected capability receives `id, goal, owner, priority, status, dependencies, risk, intended_experience, verification, evidence`. Do not fabricate evidence or assume every project requires all domains.