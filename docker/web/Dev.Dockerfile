FROM python:3.12-alpine3.21 AS build

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /buscapet
COPY ./pyproject.toml ./pyproject.toml
RUN ["uv", "sync"]


FROM build
WORKDIR /buscapet
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

COPY ./app /buscapet/app
COPY ./scripts /buscapet/scripts

EXPOSE 8000

RUN ["chmod", "+x", "/buscapet/scripts/entrypoint.sh"]

ENTRYPOINT ["sh", "./scripts/entrypoint.sh", "dev"]
