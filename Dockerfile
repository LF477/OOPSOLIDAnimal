# syntax=docker/dockerfile:1

################################################################################
# Pick a base image to serve as the foundation for the other build stages
FROM python:3.13.0b1-alpine3.19 as base

################################################################################
# Create a stage for building/compiling the application.
FROM base as build
ADD . /app
WORKDIR /app
RUN python -m ensurepip
RUN python -m pip install --upgrade pip
RUN python -m pip install flake8 pytest pytest-cov coverage
# if ( Test-Path -Path .\requirements.txt ) {pip install -r .\requirements.txt}

RUN flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
RUN flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics


################################################################################
# Create a final stage for running your application.
FROM base AS final

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
USER appuser

COPY --from=build /app /app

# What the container should run when it is started.
WORKDIR /app
CMD [ "python", "test_APP.py" ]
