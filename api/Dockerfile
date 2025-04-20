# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY main.py .

# Install dependencies
RUN pip install --no-cache-dir "fastapi[standard]>=0.115.12" uvicorn

# Expose port for the API
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
