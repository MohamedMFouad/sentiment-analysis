FROM python:3.8  # Replace with appropriate Python version

WORKDIR /app

COPY requirements.txt ./  # Copy requirements.txt if using external dependencies
RUN pip install -r requirements.txt  # Install dependencies if needed

COPY . .

EXPOSE 3040  # Replace with the desired port for the sentiment service

CMD ["python", "wsgi.py"]
