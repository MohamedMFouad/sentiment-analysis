FROM python:3.9

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip 

WORKDIR /app

 

COPY . .

EXPOSE 3041  

CMD ["python", "wsgi.py"]
