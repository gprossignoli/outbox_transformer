FROM python:3.10.9-slim-buster

RUN mkdir /app \
    && mkdir /venv \
    && adduser -u 1000 --gecos "" --disabled-password general_user

ARG development
ENV DEVELOPMENT $development

WORKDIR /app

COPY . /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pip --no-cache-dir install pipenv \
    && chown -R general_user:general_user /venv \
    && chown -R general_user:general_user /app

USER general_user

RUN virtualenv /venv

RUN if [ "$DEVELOPMENT" = "True" ]; \
    then \
        pipenv install --ignore-pipfile --dev --deploy; \
    else \
        pipenv install --ignore-pipfile --deploy; \
    fi

CMD ["pipenv", "run", "python", "app.py"]
