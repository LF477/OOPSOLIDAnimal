# syntax=docker/dockerfile:1

################################################################################
FROM python:3.13.0b1-alpine3.19

ADD . .

CMD [ "python", "test_APP.py" ]
