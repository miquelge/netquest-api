FROM python:3.10

WORKDIR /

COPY ./requirements/prod.txt /code/requirements/prod.txt

RUN pip install -r /code/requirements/prod.txt

COPY ./app /app

WORKDIR /

CMD ["uvicorn", "app.main:app", "--reload", "--log-level", "debug", "--host", "0.0.0.0", "--port", "8000"]
