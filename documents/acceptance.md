# Acceptance report

**Team:** to fill in. **Date:** to fill in. **Run by / reviewer:** to fill in.
**Application commit:** to fill in. **API/web digests:** to fill in if built.
**Deployment context and configuration commit:** to fill in.


## 1. Execution conditions

State laptop or VM, useful versions, **dedicated database**, starting data and
**preconditions**. Never write a password, full DSN, key or kubeconfig.
**Integration tests** use a database ending with _test; describe
the cleaning strategy and its protection before any deletion.

## 2. Results per requirement

| Reference ID | **Preconditions** | Action / command | Expected | Observed | Evidence | Result |
|---|---|---|---|---|---|---|
| Taken from the **grading scale** | Initial state | Reproducible action | Contract | Actual finding | File/link | Status |

Allowed results: passed, failed, **not run**, **not applicable with a reason**.
Never replace an observation with the **expected result**. If a command
was not run, write not run even if its syntax looks correct.

## 3. Example of how to write a case

**Method example to run, not a result already obtained:**

- **Precondition:** dataset created, file `data/room-measurements-2026-10-05.csv` already ingested (63 measurements).
- **Action:** upload the same file a second time, then run the worker.
- **Expected:** upload `succeeded` with 0 accepted and 63 duplicates; `measurement_count` **still equal to 63 when read back**.
- **Observed:** to complete after running.
- **Evidence:** request, response and the following read in the same environment.
- **Conclusion:** to complete; an assertion on the `succeeded` status alone is not enough.

## 4. Deployment and recovery experiments

For each experiment, keep the ids and data before/after:

- Compose **persistence**: witness UUID and **volume** kept after recreation.
- API **reconciliation**: previous/replacement Pod and observed ready states.
- **Database failure:** liveness, readiness, business requests and recovery.
- **Cloud:** consistent version, VM context and image references.
- **Rollback:** old API and web release actually back.
- **Restore:** separate target database, UUID/content found and duration measured.

State the transient errors and the limits of each experiment.
A results table does not force you to conclude that everything worked.

## 5. Known anomalies

| ID | Minimal reproduction | Expected/observed | Impact | Priority | Fix or workaround | State |
|---|---|---|---|---|---|---|
| To fill in | Data and steps | Precise gap | User/technical | Reason | Action | Open/closed |

A fix is closed after a new check of the affected scenario.
Link the result to its **commit** to avoid attributing old evidence
to a newer, untested version.

## 6. Submission summary

List the passed criteria, the remaining gaps, the operations not run and the limits.
State where to find the redacted evidence and which version the jury must assess.

## How to annotate evidence

Give an explicit name to each kept output: session, scenario and version.
Shared convention of the course: `proofs/sN-topic.ext`, for example
`proofs/s3-persistance.txt`, `proofs/s4-reconciliation.txt`,
`proofs/s6-overlay-s5.yaml` or `proofs/latence-k3d.json`. Private files
(dump, unredacted outputs) go only into `proofs/private/`, ignored by Git.
Add one sentence saying what the reader must observe. Example of form:
"In the read-back response, compare the dataset id, its number of measurements and its checksum with those recorded before
the recreation." Then complete with your values and your **actual result**.

Never use a course example as an **observed result**. Redact secrets,
but keep the statuses, fictitious dataset ids and messages useful
to understand the scenario.
