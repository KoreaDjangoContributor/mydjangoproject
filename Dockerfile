# Django 빌드
FROM python:3.8

RUN echo "django build start"

ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.8.2

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000 --timeout 60"]
