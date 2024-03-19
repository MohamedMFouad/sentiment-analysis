Dockerfile
FROM python:3.8  # Replace with appropriate Python version

WORKDIR /app

COPY requirements.txt ./  # Copy requirements.txt if using external dependencies
RUN pip install -r requirements.txt  # Install dependencies if needed

COPY . .

EXPOSE 3041  # Replace with the desired port for the proxy service

CMD ["python", "wsgi.py"]
