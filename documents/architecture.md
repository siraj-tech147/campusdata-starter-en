# Design file - team to fill in

**Members:** to fill in. **File version / commit:** to fill in.
**Review date:** to fill in. **Reviewer:** to fill in.

This template is filled in from S1 and then evolves with the decisions actually made.
Replace the instructions with your answers; keep the useful limits.
Do not copy the whole assignment: explain how it applies to your work.


## 1. Need and users

Write five sentences: 
* user - The data team uses the data
* problem - Currently, the team manually copies sensor data from CSV files into spreadsheets, which leads to errors, duplicate measurements and difficulties managing the data.
* main - Users create datasets, upload CSV files containing sensor measurements, check rejected records and view air-quality indicators for each room.
* action - Users create datasets, upload CSV files containing sensor measurements, check rejected records and view air-quality indicators for each room. 
* Excluded - The application doesnt take the data automatically. We are giving the data manual.
* Proposed - It should be take automatically from the sensors and clean the data.

## 2. Backlog and acceptance criteria

US01|As a data team member, I want to create a dataset so that I can organize campus sensor measurements.|High|Given I am on the dataset page, when I enter a valid unique name and create the dataset, then it appears in the dataset list.|Member A|Dataset creation test and screenshot

Plan a negative criterion when a refusal is expected. A task is only
finished after its result has been observed and reviewed.

## 3. Mockups and interactions

Insert the main screen and the editing screen. Annotate fields, labels, buttons and messages.
Document the empty, loading, success and error states as well as the keyboard journey.
Describe what stays filled in after a failure, the deletion confirmation and
the absence of request when the user cancels.

## 4. Architecture and flows

Produce the component, creation sequence and deployment diagrams.
Add a sequence of a refused transition with the location of the **rollback**.
Show the ports, network names, laptop/container/VM boundaries and **durable storage**.

| Context | User entry point | API access | Database access from the API | Storage location |
|---|---|---|---|---|
| Development | To record | To record | To record | To record |
| Compose | To record | To record | To record | To record |
| **k3d** | To record | To record | To record | To record |
| AWS/K3s | To record | To record | To record | To record |

## 5. Data and contract

Present the dictionary of the three tables (datasets, ingestions, measurements),
types, **SQL constraints**, foreign keys and **default values**. Explain who
produces UUIDs and **timestamps**, which values can be null, and which
uniqueness constraint makes ingestion idempotent.

Add the upload status matrix, the CSV line check rules,
the routes and HTTP examples: dataset creation, accepted upload (202), refused retry
(409), file too large (413) and deletion without response body.
Explain 404, 409, 413, 415, 422, 503 and how an unexpected error is handled.

## 6. Code layout and transactions

| Module | Responsibility | Dependencies | Important invariant/comment | Associated test |
|---|---|---|---|---|
| To fill in | One precise responsibility | Modules used | Protected rule | Scenario |

State who owns the **commit**, the **rollback**, how sessions are closed,
the **row lock** and serialisation. Describe the explicit initialisation and
the limit of create_all when the schema changes.

## 7. Argued decisions

| Decision | Option kept | Alternative studied | Concrete reason | Consequence/limit | Evidence or reference |
|---|---|---|---|---|---|
| To fill in | Choice | Alternative | Constraint satisfied | Cost or risk accepted | Reference |

A preference alone does not justify a choice. Link the decision to time,
the contract, reproducibility or the observed behaviour.

## 8. Risks and measures

| Risk | User effect | Detection | Planned measure | Remaining limit |
|---|---|---|---|---|
| API failure | To complete | To complete | To complete | To complete |
| Database failure | To complete | To complete | To complete | To complete |
| Loss of the node | To complete | To complete | To complete | To complete |
| Exposed **secret** | To complete | To complete | To complete | To complete |
| Forgotten cloud resource | To complete | To complete | To complete | To complete |

## 9. Cross review

Write down who reviewed the file, which ambiguities were found and fixed.
Identify the differences between the initial design and the final implementation.
Keep the unresolved questions and their effects, without presenting them as validated.

## Example of justification to adapt

**Example of form, to link to your work:** "We use one session
per request to separate users' transactions. The dependency closes
the session even if an error is raised. We check that ingestion is
idempotent by uploading the same file again and then reading the number of measurements."

Add the name of your module, the matching test and the observed limit.
Do not reuse this explanation if your implementation uses another
organisation: describe how it really works instead.
