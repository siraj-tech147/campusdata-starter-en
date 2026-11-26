"""CampusData API package.

This file identifies the app package. It has no start-up effect:
never start Uvicorn, open a transaction or create the schema on import.
Entry points: app.main:app (API); in S2, app.init_db (schema) and app.worker (ingestion).
"""
