# STUDENT CONTEXT: S3 | build context ./api from the root of your repository
# TO PREPARE / ADAPT: Adapt the copied code and provide APP_VERSION; never put a secret in it.
# EXPECTED CHECK: Inspect UID, served version and stack start-up after building.
#
# Preparation stage: build the wheels of the locked dependencies.
# The build runs with ./api as context; the COPY paths depend on it.
FROM python:3.12-slim-bookworm AS builder
WORKDIR /build
# Copying the lock before the code reuses the cache when only app/ changes.
COPY requirements.lock .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.lock

# Separate runtime image: only copy what is needed to run.
# Use a base compatible with the wheels of the builder stage.
FROM python:3.12-slim-bookworm AS runtime
# Avoid .pyc files and send logs unbuffered to the standard output.
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
# Stable UID, reused by the Kubernetes securityContext; no need for root.
RUN useradd --uid 10001 --create-home appuser
COPY requirements.lock .
COPY --from=builder /wheels /wheels
# Install from the copied wheels; --no-index avoids any access to the pip registry.
# Clean the working folder; the data of the previous COPY stays
# in its layers. Measure the final size rather than assuming a gain.
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.lock \
    && rm -rf /wheels
COPY --chown=10001:10001 app ./app
# Non-secret build argument: pass the full SHA of the delivered commit.
# A runtime variable does not automatically replace this VERSION file.
ARG APP_VERSION=dev
RUN printf '%s\n' "$APP_VERSION" > /app/app/VERSION
# All the following runtime commands run as this user.
USER 10001:10001
# Document the process port; EXPOSE publishes no port on the laptop.
EXPOSE 8000
# JSON form: Uvicorn receives the container's stop signals directly.
# 0.0.0.0 listens on the container's interfaces, not only on its loopback.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
