## Vision

Imagine you are new to a university or visiting a friend’s university and you want to know what are the best possible places to go eat. This is where we come in, we want to make the process of finding a suitable restaurant or food joint as frictionless as possible, while also fitting the requirements of the group. These requirements can be distance from user’s current location. It can be price, amount or the type of food/dishes. 

The end image of the app/webapp is not yet defined. Feel free to send Feature Requests and we will accept them if they belong in the app. Though the end image of the system is not yet defined we do still have some guidelines. 

## Guidelines

#### Atomic Features & Code

Features within the application should be designed to be self-contained, with clear boundaries and minimal dependencies on other components or features. Each atomic feature performs a single, well-defined function without requiring complex interconnections that could complicate maintenance or testing. This approach simplifies debugging, enhances scalability, and makes it easier for teams to collaborate effectively, ensuring changes in one area don’t inadvertently impact unrelated functionality.

#### Prevent Work Duplication

Before starting work on a new issue or feature request, conduct a thorough review of existing issues, pull requests (PRs), and documentation to determine if the task has already been addressed. This practice helps avoid redundant effort, ensures consistency across solutions, and reduces confusion that may arise from overlapping changes. When reviewing, consider both similar past implementations and recent updates to confirm no prior work is applicable or needed.

#### Work Only on Approved Feature Requests/Issues

Ensure all development efforts align with officially approved feature requests, open issues, or project roadmaps. Before committing code or creating PRs, verify that the task has received proper sign-off from relevant stakeholders—such as product managers, technical leads, or team approvals and is documented in the appropriate tracking system (e.g., GitHub Projects). This discipline prevents off-track work, minimises scope creep, and keeps development focused on prioritised objectives. 

#### Don’t Just Drop a Link include Context

Avoid posting third-party links (such as Discord) without sufficient context. When referencing external discussions that influenced your work. Like private conversations, extract and include key details directly in the GitHub issue or PR. This ensures reviewers can understand the background without leaving GitHub, while still avoiding sharing sensitive information.

#### Treat it like Documentation

GitHub serves as a central, authoritative record of our project’s evolution. Each bug report and pull request enriches our collective knowledge over time. When documenting changes or decisions, aim for clarity so that even after several months, someone including yourself can easily revisit the content and grasp both what was done and why it was done that way.

#### Think like a reviewer

Think like a reviewer in terms of code complexity, code quality. Considering the future implications, it’s important to acknowledge any trade-offs, edge cases, and temporary solutions upfront. clearly documenting these aspects will help prevent misunderstandings or oversight down the line.

#### Show your testing

Describe how you verified your modifications. You don't need a complete or detailed account. only enough information to assure reviewers that the changes were thoroughly checked and function as intended.

> Example:  
>“Tested locally with mock data and confirmed the flow works on staging.”

#### Submitting PRs

- Please ensure your code is linted and cleaned before submitting. 

### Codebase specific instructions

#### WebApp (next.js)

- use nextjs code conventions
- use biome as the linter (run  bun run lint before submitting)
- refer to frontend/README.md for more instructions

#### backend (Django)

- use Django conventions
- use ruff as a linter (run uvx ruff format before submitting)
- refer to backend/README.md for more instructions
