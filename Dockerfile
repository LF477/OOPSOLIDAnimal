# syntax=docker/dockerfile:1

################################################################################
FROM python:3.13.0b1-alpine3.19

ADD . .

RUN pip install pytest
RUN ls -al
RUN sudo chmod +x /test_APP.py
# ENTRYPOINT ls -al
ENTRYPOINT pytest
