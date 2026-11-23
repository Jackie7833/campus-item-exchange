FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

WORKDIR /app

COPY requirements-cloud.txt ./requirements-cloud.txt
RUN pip install --no-cache-dir -r requirements-cloud.txt

COPY . .

EXPOSE 8080

CMD ["sh", "-c", "gunicorn -w 2 -b 0.0.0.0:${PORT:-8080} wsgi:app"]
