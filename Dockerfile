FROM python:3.11-slim

RUN sudo apt update -y build-essential libpq-dev gcc

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry 

RUN poetry config virtualenvs.create false \ && poetry install --no-interception --no-ansi

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--env-file", ".env" ]