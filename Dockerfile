FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install -U fastapi loguru 
COPY ./app /app

EXPOSE 5678
EXPOSE 8080
