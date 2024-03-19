# Base image for Python environment (choose appropriate version)
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy requirements.txt (if using external dependencies)
COPY requirements.txt ./

# Install dependencies (if using requirements.txt)
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose the port (replace 3041/3040 with actual ports)
EXPOSE 3041

# Command to run the application
CMD ["python", "app.py"]
