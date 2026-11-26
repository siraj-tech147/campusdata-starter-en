# Operational README template - to fill in

In session 6, this content replaces the starter's `README.md` at the root of your
repository. It is written for someone who attended no session: they must
be able to install, check, update, restore and clean up without any oral explanation.
Delete the instructions in italics once the section is written.


**Team:** to fill in. **Commit described:** to fill in.
**Assessed release (API/web images by digest):** to fill in.

## 1. Need and architecture

_Three to five sentences on the need, then the browser - Nginx - API -
PostgreSQL diagram with the durable storage. Link to `documents/architecture.md`._

## 2. Known limits of the prototype

_No authentication, one node, a single-replica database, local storage, access through
a tunnel. Add the open anomalies from `documents/acceptance.md`._

## 3. Prerequisites

| Tool or access | Checked version | Check command |
|---|---|---|
| Python | To record | `python3.12 --version` |
| Docker / Compose | To record | `docker version`, `docker compose version` |
| k3d / kubectl | To record | `k3d version`, `kubectl version --client` |
| AWS and GHCR accounts | Region, permissions | See preparation |

## 4. Procedures

Each procedure follows the same format. Never write a secret in this file.

| Section | Where (laptop/VM/container) | Starting folder | Prerequisites and variables | Commands | Expected result | Diagnosis on failure |
|---|---|---|---|---|---|---|
| Generate `.env` | Laptop | Root | No existing `.env` | To fill in | File 600 ignored by Git | `git check-ignore .env` |
| Local development | Laptop | Root then `api/` | `.env`, venv | To fill in | live/ready 200 | To fill in |
| Isolated tests | Laptop | Root then `api/` | DSN to `campus_test` | To fill in | Number of passing tests | To fill in |
| Schema initialisation | Depends on environment | To fill in | Database ready | To fill in | Two runs without loss | To fill in |
| Full Compose | Laptop | Root | `.env` reloaded (`db`) | To fill in | Healthy stack, upload processed by the worker | To fill in |
| Local Kubernetes | Laptop | Root | Context `k3d-campusdata` | To fill in | 2 Ready APIs, PVC Bound | To fill in |
| Image publication | Laptop or CI | Root | GHCR login | To fill in | Two digests recorded | To fill in |
| Cloud deployment | VM | `~/campusdata` | `kubectl` function, Secret | To fill in | Expected version served | To fill in |
| SSH tunnel | Laptop | Any | `CAMPUS_KEY`, `CAMPUS_HOST` | To fill in | Page on 8082 | To fill in |
| Update (promotion) | Laptop then VM | Root / `~/campusdata` | Green CI run, digests | To fill in | Rollout finished, version | To fill in |
| Rollback | Laptop then VM | Root / `~/campusdata` | Previous overlay kept | To fill in | Old version, data | To fill in |
| Backup | VM then laptop | `~` / root | Witness dataset recorded (id, number of measurements) | To fill in | Non-empty dump outside the VM | To fill in |
| Restore | VM | `~` | Dump available | To fill in | Identical witness in `campus_restore` | To fill in |
| Cleanup | AWS console, laptop | - | Evidence exported | To fill in | Empty inventory or exceptions | To fill in |

## 5. Evidence and acceptance

_Link to `documents/acceptance.md`, the `proofs/` folder and the naming convention.
State which evidence matches the assessed release._

## 6. Provided work and team work

_List the templates received from the kit, what the team wrote or adapted, and the
outside help declared in `documents/journal.md`._
