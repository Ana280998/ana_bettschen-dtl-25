FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir streamlit python-dotenv

EXPOSE 8501

CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]

