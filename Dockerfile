# Pull a base image
FROM python:3.8-slim-buster
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

# Create a working directory for the django project
WORKDIR /miu
# Copy requirements to the container
COPY Pipfile Pipfile.lock /miu/

# Install the requirements to the container
RUN pip install pipenv && pipenv install --system
# Copy the project files into the working directory
COPY . /miu/
# Open a port on the container
EXPOSE 8000
