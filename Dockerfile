    FROM python:3.12.4-slim

    WORKDIR /app

    COPY ../src/ /app

    RUN apt-get update && apt-get install

    ENV PATH="/root/.local/bin:$PATH"

    RUN pip install poetry

    RUN poetry install

    ENTRYPOINT  ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
