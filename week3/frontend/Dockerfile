FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY frontend.py .

EXPOSE 8502

CMD ["streamlit", "run", "frontend.py", "--server.port=8502", "--server.address=0.0.0.0"]