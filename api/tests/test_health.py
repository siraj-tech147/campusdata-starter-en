# STUDENT CONTEXT: S1-S2 | tests run in your Python environment
# TO PREPARE / ADAPT: Set DATABASE_URL before pytest; keep campus_test for the business tests.
# EXPECTED CHECK: Read the number of tests and the assertions: two tests validate neither the business API nor ingestion.
#
"""Smoke tests of the starter, to be completed with the business acceptance in session 2.

DATABASE_URL must be set before app.main is imported, even if these two
routes do not query PostgreSQL. The business tests use campus_test.
Never reset a database whose name does not end with _test.
"""
from fastapi.testclient import TestClient

from app.main import app

# TestClient calls the application inside the test process, without starting
# Uvicorn, Nginx, Docker or a TCP server. Success here does not test the network.
client = TestClient(app)


def test_liveness():
    """The minimal process health contract stays available without SQL."""
    assert client.get("/health/live").json() == {"status": "ok"}


def test_version():
    """The version route exposes the key expected by the release check."""
    assert "version" in client.get("/api/version").json()

# TODO S2: complete with the business tests on PostgreSQL (campus_test).
# Organise each scenario as preparation, action, observable check.
# Ingestion: use the files of data/ and check the counters
# accepted / rejected / duplicates, then the absence of duplicates after a second upload.
# Deleting a dataset: 204 without body, then 404 and no linked measurement left.
# Readiness: test a missing database and a missing table separately.
# These two tests alone validate neither persistence, nor business logic, nor deployment.
