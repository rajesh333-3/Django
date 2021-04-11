# base image  
FROM python:3.8   
# setup environment variable  
#DockerHOME=/app 

WORKDIR /app

ADD . /app

ENV PYTHONUNBUFFERED 1  

COPY . /app 

#COPY ./requirements.txt /app/requirements.txt
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
#EXPOSE 5000  
# start server  
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT