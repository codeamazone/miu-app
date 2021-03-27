# MIU

## Magical Idea Universe

![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

A Django app that helps you manage and keep track of your ideas and visions.

![screenshot](static/img/screenshot_list.png)

Sort your ideas according to their name, kind (project, vision, try something), status (pending, in progress, completed), idea description and next steps.

## Detail view

The detail view shows you the details of an idea
![screenshot](static/img/screenshot_detail.png)

## Update View

Via the update view you can edit the details of your selected idea.
![screenshot](static/img/screenshot_update.png)

## How to use locally on your computer

- Download and install [Python](https://www.python.org/downloads/)
- install Pipenv

```
pip3 install pipenv
```

- open the project folder in your bash and install the latest version of Django with Pipenv

```
pipenv install django
```

Activate the virtual environment

```
pipenv shell
```

- Create a file named .env
- Get a secret key (for example on https://miniwebtool.com/django-secret-key-generator/)
- Enter the secret key in the .env file like this (enter your secret key where it says 'secret_key'):

```
export SECRET_KEY='<secret_key>'
```

- Migrate

```
python manage.py makemigrations ideas
```

```
python manage.py migrate
```

- Start the server

```
python manage.py runserver
```

## The project is a work-in-progress and will be updated continuously.
