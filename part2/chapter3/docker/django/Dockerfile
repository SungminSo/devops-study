FROM python:3.6.7

ENV PYTHONPATHBUFFERD 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/docker-django
ADD . /srv/docker-django

WORKDIR /srv/docker-django

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
