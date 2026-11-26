# STUDENT CONTEXT: S1-S2 | Uvicorn entry point app.main:app
# TO PREPARE / ADAPT: Load DATABASE_URL before starting. Complete the TODOs according to the contract.
# EXPECTED CHECK: Check live/ready/version, then the business routes once you have built them.
#
"""Entry point of the CampusData base, to be completed during session 2.

The starter only exposes process health, database access and the version.
It contains no tables (datasets, ingestions, measurements), no business
routes, no CSV reading and no ingestion worker.
In S2, move the connection to database.py and include the business router.
Keep a single configuration source for the probes and the services.
"""
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# This version describes the OpenAPI contract; /api/version identifies the release.
app = FastAPI(title="CampusData", version="0.1.0")
# The variable must exist BEFORE the module is imported, including under pytest.
# Its host depends on the context: laptop = 127.0.0.1; Compose/Kubernetes = db.
# The engine manages the connection pool. It is not a transaction Session.
engine = create_engine(
    os.environ["DATABASE_URL"],
    # Checking connections taken from the pool helps after a database outage.
    # It does not automatically replay an interrupted transaction.
    pool_pre_ping=True,
    # Bound the connection set-up; this is not a global SQL timeout.
    connect_args={"connect_timeout": 3},
)


@app.get("/health/live")
def live():
    """Check the process without depending on PostgreSQL availability."""
    # A database outage must change readiness, not cause a restart loop
    # of an API process that still works.
    return {"status": "ok"}


@app.get("/health/ready")
def ready():
    """Check the database connection; add the table check in session 2."""
    try:
        # The context releases the connection even when an exception is raised.
        with engine.connect() as connection:
            # SELECT 1 proves a connection, not the existence of the business schema.
            # TODO S2: also read datasets, ingestions and measurements
            # (SELECT 1 FROM <table> LIMIT 1). An empty table is still valid.
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        # Generic public response: never return the DSN or the secret.
        # This interception is limited to the probe. In the business routes, tell apart
        # database unavailability, business conflict and programming error.
        raise HTTPException(status_code=503, detail="Database unavailable") from None
    return {"status": "ready"}


@app.get("/api/version")
def version():
    """Read the reference written at build time, or dev when run locally."""
    # The path is relative to the module, not to the terminal's current folder.
    version_file = Path(__file__).with_name("VERSION")
    value = version_file.read_text().strip() if version_file.exists() else "dev"
    # The version allows a cross-check with the commit and the digest.
    # This field alone does not prove that the whole acceptance was run.
    return {"version": value}

# TODO S2: models.py, schemas.py, database.py, services.py, routes.py.
# TODO S2: ingestion.py (CSV reading and checks) and worker.py (processing
#          of pending uploads, outside the API process).
# TODO S2: one Session per request; close and rollback on failure.
# TODO S2: explicit initialisation in app/init_db.py, outside API start-up.
# TODO S2: include the /api/datasets and /api/ingestions routers.
