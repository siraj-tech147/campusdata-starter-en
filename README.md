# CampusData starter kit

This folder is a **teaching starter**, not the finished application. CampusData ingests CSV files of air quality measurements (CO₂, temperature, humidity) and computes indicators per room. The business routes, the ingestion worker and the **interface** are built in session 2 according to the assignment. The infrastructure configurations are provided to be adapted, run and explained.

This is the English kit: it contains exactly the same code and files as the French kit; only the comments, the page texts and the documents are translated. Some file names are translated too (for example `data/room-measurements-2026-10-05.csv` and `documents/acceptance.md`); the English pages of the course always use these English names.

## Usage

1. Copy the whole folder into a separate **student repository**, hidden files included.
2. Read the assignment and the preparation in the course.
3. Generate `.env`, create the Python 3.12 **venv** and install `api/requirements-dev.lock`.
4. S1: start **PostgreSQL** with `compose.dev.yaml`, run the base API on the laptop.
5. S2: develop `models`, `schemas`, `services`, `routes`, `database`, `init_db`, `ingestion` and `worker`, then the interface and the tests with the files of `data/`.
6. S3: use `compose.yaml` with containerised API, worker and web.
7. S4: apply the Kubernetes manifests, including the ingestion CronJob, after importing the images into k3d.
8. S5: publish the images and create a cloud overlay pointing to their digests.
9. S6: copy `github-workflows/ci.yaml` to `.github/workflows/ci.yaml` and adapt it to the **business tests**; write the final README from `documents/delivery-readme.md`.

## What works from the start

- `/health/live`: process health.
- `/health/ready`: **PostgreSQL** connection only; add the check of the three tables in S2.
- `/api/version`: `dev` outside an **image**, or the version written at build time.
- Two base tests: they validate neither the business API nor ingestion.
- Three fictitious CSV files in `data/`: a valid file (63 measurements), a file mixing valid lines, invalid lines and a duplicate, a file with an invalid header.
- Supporting **images**, network and manifests, depending on the tools and registry available.

## Work to do

- Dataset, Ingestion and Measurement models, **Pydantic** contract, transactions and upload lifecycle.
- CSV reading and checking, idempotent insertion, rejection report and indicators per room.
- **Worker** `python -m app.worker` (loop) and `--once` (a single pass, used by the CronJob).
- **Explicit initialisation** `python -m app.init_db`; this module deliberately does not exist yet.
- **Interface**, error states and **business tests** on a dedicated PostgreSQL database.
- Real configuration, documentation, evidence and operations.

## Configuration markers

| API context | Database host | Database | Browser entry point |
|---|---|---|---|
| API on the laptop (S1-S2) | `127.0.0.1` | `campus` | `http://127.0.0.1:8080` through `web/dev.conf` |
| Tests on the laptop | `127.0.0.1` | `campus_test` | None: pytest calls the API inside the process |
| Compose (S3) | `db` | `campus` | `http://127.0.0.1:8080` |
| **Kubernetes** k3d (S4) | `db` | `campus` | `http://127.0.0.1:8081` |
| K3s on EC2 (S5-S6) | `db` | `campus` | `http://127.0.0.1:8082` through an SSH tunnel |
| CI | `localhost` | `campus_test` | None |

The course's "Cheat sheet" page gathers ports, variables and check commands for each environment.

Base **image** tags are used for the teaching start; record and pin the **digests** for promotion. Python locks are included. `pyproject.toml` sets the Ruff rules and lets pytest resolve the `app` package from the root or from `api/`. Regenerate the locks together after a dependency change, then check installation and tests.

## Secrets and generated files

`.env.example` contains placeholders. `.env`, dumps, keys and kubeconfigs are ignored by Git. Never publish the real values in the documents. Do not use `docker compose down -v` or delete a **PVC** before backing up the useful data.

The `documents/` templates are filled in throughout the sessions. Once built, replace this starter README with your operational README, while stating the templates received and the team's work.

## Read the templates in a useful order

Comments explain intentions, dependencies and limits.
They do not replace checking the behaviour after adaptation.

| File or group | To understand before changing it | Student work | **Expected evidence** |
|---|---|---|---|
| `api/app/main.py` | Engine, probes and VERSION file | Extract database access, complete **readiness**, include the business routes | Routes and health compliant |
| `api/tests/test_health.py` | In-process tests, without a real network | Add **business tests** and **PostgreSQL** isolation | Results and database state checked |
| `api/requirements*.in` and locks | Direct dependencies and resolved versions | Keep the locks consistent | Reproducible installation |
| `api/Dockerfile` | Build/runtime, wheels, user, version | Explain and adapt the necessary files | UID, **image** and version observed |
| `api/.dockerignore` | API context and exclusions | Check the files entering the build | No **secret** in the context |
| `web/index.html` | Structure, labels, messages, JS loading | Create forms and interactions | Keyboard journey and UI states |
| `web/app.js` | Implementation plan and **HTTP contract** | Implement requests, rendering and changes | 204/422/409/network handled |
| `web/styles.css` | Readability, focus and states | Complete without hiding the focus | Readable and usable display |
| `web/dev.conf` | API on the laptop through the containerised proxy | Check the development path | **Same origin** in S2 |
| `web/default.conf` and **Dockerfile** | Internal API and embedded files | Include every delivered asset | Rendering and API calls in the **image** |
| `compose.dev.yaml` | Database/proxy in **containers**, local API | Adapt the local environment | Database reachable on the laptop |
| `compose.yaml` | Four services (db, api, worker, web), health, ports and **volume** | Validate initialisation order and recovery | Persistent witness |
| `.env.example` and `.gitignore` | Placeholders and unversioned files | Generate the real values **outside Git** | Review before **commit** |
| `k8s/00-namespace.yaml` | Scope of the objects | Check the target context | Correct **namespace** |
| `k8s/10-config.yaml` | Non-secret configuration | Create the **Secret** separately | Consistent references |
| `k8s/20-db.yaml` | **PVC**, single server and Recreate | Explain storage and interruption | Data after replacement |
| `k8s/30-api.yaml` | **Replicas**, permissions, probes and resources | Check the health behaviour built in S2 | **Reconciliation** and availability |
| `k8s/35-worker.yaml` | CronJob, `--once`, concurrency forbidden | Check the image and the Secret; observe a Job | `pending` upload processed in under 2 min |
| `data/*.csv` | Expected format and error cases | Use these files in the tests and acceptance | Counters matching the contract |
| `k8s/40-web.yaml` | Web **image** and **Service** | Check files and network | Page, then upload and indicators successful |
| `k8s/50-ingress.yaml` | Routing to web through Traefik | Check the local/cloud entry | Access at the planned point |
| `k8s/kustomization.yaml` | Assembly of the resources | Create the cloud overlay in S5 | Final **images** by **digest** |
| `github-workflows/ci.yaml` | Job dependencies and publication conditions | Move to the right path, initialise the database, test the business logic | Traceable run and **images** |
| `pyproject.toml` | Test discovery and Ruff rules | Run the checks from the student project | Lint and pytest successful |
| `documents/` | Templates to fill in, not results already validated | Write throughout the sessions | Reproducible and honest file |
| `documents/delivery-readme.md` | Sections of the final README required in S6 | Replace this starter README in S6 | README followed by another team |

## Turn a TODO into checked work

1. Find the rule in the **shared contract** and a positive/negative example.
2. Identify the responsible file; do not put all the logic in main.py.
3. Write the smallest operation that respects this contract and the expected errors.
4. Add the observable check; read the data back after a refused change.
5. Integrate with the neighbouring component, then do the user journey.
6. Replace the finished TODO with a comment of intent if necessary.
7. Record **commit**, result and limit in the acceptance report.

The kit deliberately does not contain `models.py`, `schemas.py`, `services.py`,
`routes.py`, `database.py`, `init_db.py`, `ingestion.py` or `worker.py`. These files are produced in S2: the session 2 page gives, for each of them, tested starting code, the `TODO` parts to write and a solution to look at if you are stuck.
The initialisation commands of the following sessions only work after
they are built. Do not hide their absence with an empty script that returns 0.

## Comment without making the code unreadable

Put the comment close to the decision it explains. Prefer one sentence
about the invariant to ten lines describing each assignment. For important
functions, a docstring describes role, result and significant errors.
In YAML, explain the links between fields and the lab's assumptions.

Examples of questions your comments must answer:

- Why one **Session per request**, closed even on error?
- Why must the same file uploaded twice not create duplicates?
- Why does the worker lock the upload with SKIP LOCKED?
- Why does **liveness** not query **PostgreSQL**?
- Why must the database volume outlive the container?
- Why can a Running Pod be not ready?
- Why does a successful pipeline not deploy to the VM automatically?

Never put a secret value in a comment. A comment is versioned
text, sometimes embedded in the **image**, like the code it comes with.

## Read the getting-started comments

The editable files state **STUDENT CONTEXT**, **TO PREPARE / ADAPT**
or **TO BUILD**, then **EXPECTED CHECK**. Read these three markers before
any change: they separate the file's role, your work and the evidence
to produce. The comments can be kept in your repository.

The requirements.lock and requirements-dev.lock files are generated: their
original comments and their via lines describe how the dependencies were resolved.
Do not annotate them by changing versions at random. Your change intentions
are documented in the .in files and in your journal, then you regenerate
both locks according to the preparation.

The documents/ templates offer writing examples that are explicitly to be
completed. An observation left "to fill in" is not a validation.
When you write your own procedures, also comment terminal, folder,
expected variables and the effect of the commands: your README must stay usable
by someone who has just opened their terminal.
