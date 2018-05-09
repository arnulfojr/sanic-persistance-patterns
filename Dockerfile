FROM python:3.6-alpine as mysql-based

ENV APP_DIR "/app"

ENV PYTHONPATH "${APP_DIR}/src"

ENV PATH "${APP_DIR}/bin:${PATH}"

RUN apk add --no-cache build-base

COPY ./src ${APP_DIR}/src

COPY ./requirements.txt ${APP_DIR}/requirements.txt

COPY ./requirements-mysql.txt ${APP_DIR}/requirements-mysql.txt

RUN pip3 install -r ${APP_DIR}/requirements.txt

RUN pip3 install -r ${APP_DIR}/requirements-mysql.txt

RUN apk del build-base

WORKDIR ${APP_DIR}

# Handle container as python executable
ENTRYPOINT ["/usr/local/bin/python"]

CMD ["src/run.py"]


FROM python:3.6-alpine as dynamo-based

ENV APP_DIR "/app"

ENV PYTHONPATH "${APP_DIR}/src"

ENV PATH "${APP_DIR}/bin:${PATH}"

RUN apk add --no-cache build-base

COPY ./src ${APP_DIR}/src

COPY ./requirements.txt ${APP_DIR}/requirements.txt

COPY ./requirements-dynamo.txt ${APP_DIR}/requirements-dynamo.txt

RUN pip3 install -r ${APP_DIR}/requirements.txt

RUN pip3 install -r ${APP_DIR}/requirements-dynamo.txt

RUN apk del build-base

WORKDIR ${APP_DIR}

# Handle container as python executable
ENTRYPOINT ["/usr/local/bin/python"]

CMD ["src/run.py"]
