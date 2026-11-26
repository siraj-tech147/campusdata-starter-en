# Operating CampusData

**Team / owner:** to fill in. **Last check:** to fill in.
This document must let another pair intervene without any oral explanation.
Each procedure states context, preconditions, action, expected result, check and
return to normal. Never paste a **secret** into the examples.


## 1. Inventory

| Resource | Non-**secret** id | Region/context | Owner | Role | Planned deletion |
|---|---|---|---|---|---|
| To fill in | Recorded value | Environment | Team | Purpose | Date/procedure |

Record VM, **volume**, security group, referenced public key, **namespace**,
API/web **images** and digests. Tell your own resources apart from shared ones.
Document where secrets are kept without copying their value.

## 2. Checks before intervening

- Laptop or VM and working folder: to state for each command.
- Cluster/context and **namespace**: to check before any change.
- Current version and target version: to record before promotion.
- Database state, **witness dataset** and useful **backup**: to check.
- Expected effect, interruption risk and stop condition: to explain.

## 3. Deploy a version

Describe prerequisites, available **images**, overlay rendering, transfer and application.
State when to initialise the schema and why not to wait for a business **readiness**
that depends on a table not yet created.

| Step | Place/folder | Adapted command | Expected | Check on failure |
|---|---|---|---|---|
| To fill in | Laptop or VM | **Without secrets** | Observation | Targeted diagnosis |

Conclude with API/web versions, **rollout**, processed upload and pre-existing data found again.
A created resource is not sufficient evidence of a ready **service**.

### Release sheet

Fill in one sheet per promoted or restored version. A release is only "promoted"
if the four checks of the last row are observed.

| Item | Previous release | Candidate release |
|---|---|---|
| Source commit of the images | To record | To record |
| CI run (link) and result | To record | To record |
| API image: tag and digest | To record | To record |
| Web image: tag and digest | To record | To record |
| Configuration commit (overlay) | To record | To record |
| Visible change to tell it apart | To describe | To describe |
| Time applied and operator | To record | To record |
| API/web rollout, `/api/version`, business journey, witness dataset | Observed / not observed | Observed / not observed |

## 4. Diagnose an incident

Follow: symptom - hypothesis - command - observation - fix - check.
Tell apart browser, tunnel, **Nginx**, **Service**, **Pod**, API and PostgreSQL.

| Symptom | Hypothesis | Discriminating observation | Targeted fix | Recovery check |
|---|---|---|---|---|
| To fill in | Possible cause | What confirms or refutes it | Justified action | User effect |

Keep time, duration and last change. Avoid reinstalling
or deleting storage before understanding the state of the data.

### Incident sheet

| Section | Expected content |
|---|---|
| Start / end / duration | Times recorded, not estimated afterwards |
| User symptom | What the browser or `curl` shows (HTTP code, message) |
| Observed state | Pods, events, rollout, useful logs, without secret |
| Hypothesis and evidence | Hypothesis kept and the observation that confirms it |
| Refuted hypotheses | Leads dropped and why |
| Fix | Command or change applied, where it was run |
| Recovery check | Readiness, API/web version, reading the witness dataset |
| Stop condition | What would have forced you to stop (wrong cluster, risk to the data) |
| Follow-up | Runbook improvement, test or alert to add |

## 5. Go back to the previous version

Record the old API AND web **images** and the matching configuration.
Check schema compatibility, apply the rollback and check both
components as well as the **witness dataset**. Explain the difference between repairing a
**rollout** with an invalid image and restoring a previous release.

If an imperative command is used, then reconcile the versioned
files with the desired state. An **image** **rollback** does not cancel an SQL migration.

## 6. Back up and restore

State the source database, format, VM destination, copy outside the VM and access rights.
Explain where shell redirections are interpreted and why no TTY
must alter the binary **backup** stream.

Describe the **restore** into a **separate database**, then the comparison of a witness:
dataset id, number of measurements, checksum and period covered. Require one row found, not two empty results.
Record result, duration and the bounds of the timing.

- **RPO** explained for this one-off **backup**: to fill in.
- Targeted **RTO** and actually measured duration: to fill in separately.
- Limit of a **restore** on the same server: to explain.
- Possible extension on a new server: **actual result** or not run.

## 7. Resume after a stop

Describe how to get a possible new IP, check the **K3s** service,
define the kubectl function on the VM, Pods/PVC state, tunnel and **witness dataset**.
Do not regenerate the password of an existing database by simply rerunning the initial
Secret creation block.

## 8. Close and check the resources

Export the useful evidence and backups before deletion. Identify the exact instance
and volumes; follow the session 6 procedure. Tell apart Stop,
Terminate and the handling of kept volumes, snapshots or addresses.

| Lab resource | State before | Cleanup action | State checked after | Evidence/date | Justified exception |
|---|---|---|---|---|---|
| To fill in | Recorded | Targeted action | Finding | Reference | If necessary |

State the shared resources kept, the revocation of temporary access and the
delayed check of the costs. Do not conclude that cleanup is done just because
the **SSH tunnel** is closed.

## How to write a reusable command

For each block, add a comment stating laptop or VM, starting folder,
required variables and expected effect. Someone who opens a new terminal
must know what to reload. Also say how to quit a -w watch or a tunnel,
and tell this apart from stopping the observed **service**.

For an operation on a database, a **volume** or a cloud resource, name the target
and the prior check. Put the result check right after
the action, with a diagnosis lead if this check fails.
