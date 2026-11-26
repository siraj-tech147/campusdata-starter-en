# Team journal

**Members:** to fill in. **Student repository:** to fill in.
The journal records decisions and results, not a list of copied commands.
Fill it in as you go, a few lines per step, without any **secret**.


## 1. Work and role switching

| Session/step | Driver | Navigator | Work actually done | Commit/evidence | Difficulty | Next action |
|---|---|---|---|---|---|---|
| To fill in | Member | Member | Concrete result | Reference | Symptom | Targeted action |

Show the role changes and the reviews. Each member must
be able to explain a development decision and an operations decision.

## 2. Reasoning during a blocker

- Context and **expected result**: to fill in.
- Exact observation, without **secret**: to fill in.
- Hypothesis and chosen check: to fill in.
- Result of the check: to fill in.
- Fix and recovery check: to fill in.
- Useful lesson for the **runbook**: to fill in.

A refuted hypothesis is still useful: write down why it was dropped.

## 3. Reviews and individual understanding

| Item reviewed | Author | Reviewer | Question asked | Fix/decision | Check evidence |
|---|---|---|---|---|---|
| To fill in | Member | Member | Precise point | Result | Reference |

Also check the comments: are they consistent with the code built?
Remove finished TODOs and keep those that describe remaining work.

## 4. Use of AI tools

State the help obtained, the adaptations and the checks done.

| Help needed | Suggestion received | Adaptation made by the team | Check | Limit or rejected suggestion |
|---|---|---|---|---|
| To fill in | Summary, without private data | Change understood | Test/evidence | Explanation |

The pair stays responsible for what it submits and must be able to explain it.
A generated block does not become valid without reading the contract and a real check.

## 5. Final review

Each member states a **business rule** understood, an incident diagnosed,
an infrastructure decision explained and a point they would study further.

## Example of a useful note to complete

- Step: **PostgreSQL** access from the containerised API.
- Hypothesis to check: the DSN still uses the laptop's address.
- Chosen check: compare the configured host with the network context, without publishing the DSN.
- **Observation:** to fill in after reading the useful elements.
- Fix and check: to fill in with your action and the **readiness** result.
- Commit or evidence: to fill in if a change was needed.

This example describes an approach, not an incident already seen by your pair.
A difficulty solved without a code change can be documented in the journal
and the **runbook** without inventing a fix **commit**.
