FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app/backend
COPY requirements.txt /app/backend/
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]