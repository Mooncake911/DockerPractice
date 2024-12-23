FROM python:3.9-slim

# Install dependencies
RUN pip install flask

# Set working directory
WORKDIR /app

# Copy application script
COPY app.py /app

CMD ["python", "app.py"]
