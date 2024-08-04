# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=app.py
ENV PYTHONPATH=.
ENV FLASK_DEBUG=1

EXPOSE 8080

CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]

# Run the Flask app
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]