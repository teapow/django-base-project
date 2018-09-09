# Adapted from:
#   https://github.com/dockerfiles/django-uwsgi-nginx/blob/master/Dockerfile

FROM python:3.6

MAINTAINER "Thomas Power <thomaspwr@gmail.com>"

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        sqlite3 \
        vim && \
    pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

# Install uwsgi now because it takes a little while.
RUN pip install uwsgi

# Don't write .pyc files.
ENV PYTHONDONTWRITEBYTECODE 1

# Ensure console output is not buffered by Docker.
ENV PYTHONUNBUFFERED 1

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your
# code, this will cause Docker's caching mechanism to prevent re-installing
# all dependencies when a change is made to a line or two in the app.
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add (the rest of) the code.
COPY . /app

VOLUME /app/media
VOLUME /app/static-collection
VOLUME /app/project/local_settings.py
VOLUME /app/uwsgi

WORKDIR /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]

CMD ["uwsgi", "--ini=/app/uwsgi/uwsgi.ini"]
