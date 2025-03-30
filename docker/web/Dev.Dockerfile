FROM python:3.12-alpine3.21

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir /buscapet
RUN mkdir /buscapet/app

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

COPY ./app /buscapet/app
COPY ./pyproject.toml /buscapet/pyproject.toml
COPY ./scripts /buscapet/scripts

WORKDIR /buscapet

RUN ["uv", "sync"]

EXPOSE 8000

RUN ["chmod", "+x", "/buscapet/scripts/entrypoint.sh"]

ENTRYPOINT ["sh", "/buscapet/scripts/entrypoint.sh"]
