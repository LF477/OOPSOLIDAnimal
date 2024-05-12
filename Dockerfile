# syntax=docker/dockerfile:1

################################################################################
FROM python:3.13.0b1-alpine3.19

ADD . .
RUN python -m ensurepip
RUN python -m pip install --upgrade pip
RUN python -m pip install flake8 pytest pytest-cov coverage
# if ( Test-Path -Path .\requirements.txt ) {pip install -r .\requirements.txt}

RUN flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
RUN flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
CMD [ "python", "test_APP.py" ]
