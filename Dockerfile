FROM python:3.12.8-slim AS base

ARG DEBIAN_FRONTEND=noninteractive

ENV PIP_NO_CACHE_DIR=1 \
		PIP_DISABLE_PIP_VERSION_CHECK=1 \
		POETRY_VIRTUALENVS_CREATE=1 \
		POETRY_VIRTUALENVS_IN_PROJECT=1 \
		POETRY_NO_INTERACTION=1 \
		POETRY_CACHE_DIR=/tmp/poetry_cache

RUN apt-get update \
		&& apt-get upgrade -y \
		&& apt-get install -y --no-install-recommends \
			apt-utils make kmod libpq-dev gcc ca-certificates libffi-dev \
		&& rm -rf /var/lib/apt/lists/* \
		&& pip install -U --no-cache-dir pip \
		&& pip install --no-cache-dir poetry

RUN groupadd -r resume && useradd -rm -u 7723 -g resume resume
USER resume

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry install --no-root --sync --only main && rm -rf $POETRY_CACHE_DIR

ENV PATH="/code/.venv/bin:$PATH"

COPY --chown=resume:resume ./app /code/app

USER resume

CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "4", "--threads", "4", "-b", "0.0.0.0:7070"]
