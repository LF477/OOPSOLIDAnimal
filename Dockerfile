# syntax=docker/dockerfile:1

################################################################################
FROM python:3.13.0b1-alpine3.19

ADD . .

# RUN pip install pytest
RUN ls -al
RUN chmod 777 ./test_App.py
# ENTRYPOINT ls -al
ENTRYPOINT python ./test_App.py
