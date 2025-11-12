# Jessica Backend Monorepo

This repository hosts multiple backend services and shared packages. The initial service provided is `gateway`, acting as the entry point between frontend clients and backend microservices.

## Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) (used for dependency management)

### Install Poetry (using the official installer)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
poetry --version
```

## Install Project Dependencies

From the repository root:

```powershell
poetry install --no-root
```

Poetry installs dependencies for the workspace (including `services/gateway`) and prepares a single virtual environment for all commands. The root project is not packaged—dependencies only.

## Running a Service

After installation you can launch a service directly from the root because the scripts defined in each service are exposed through the shared virtual environment.

1. Ensure you are in the repo root (`C:\Users\agame\OneDrive\Desktop\Jessica-hit-backend`).
2. Run:

   ```powershell
   poetry run gateway
   ```

   The script defined in `services/gateway/pyproject.toml` instantiates the service using configuration from `services/gateway/.env`.

### Environment Configuration

The gateway service reads values with the `GATEWAY_` prefix. Create `services/gateway/.env` if you want to override defaults.

Example:

```
GATEWAY_HOST=127.0.0.1
GATEWAY_PORT=9000
GATEWAY_LOG_LEVEL=debug
```

## Running Tests for a Service

```powershell
poetry run pytest services/gateway/tests
```

## Adding Additional Services or Packages

- Add each service under `services/<name>/` with its own `pyproject.toml`.
- Register the service in the root `pyproject.toml` as a path dependency (e.g., `service-name = { path = "services/service-name", develop = true }`).
- Run `poetry install --no-root` again to pick up new dependencies and refresh the workspace lock file.

## Troubleshooting

- If Poetry cannot find the service script, confirm that `poetry install` completed successfully and that the service is listed as a path dependency in the root `pyproject.toml`.
- Use `poetry run which python` to verify commands run inside the Poetry-managed virtual environment.

