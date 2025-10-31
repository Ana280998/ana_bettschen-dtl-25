FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir flask python-dotenv requests

EXPOSE 5001

CMD ["python", "api.py"]

