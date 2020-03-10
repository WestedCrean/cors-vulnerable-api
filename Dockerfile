FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install fastapi==0.52.0, loguru
COPY ./app /app

EXPOSE 5678
EXPOSE 8080
