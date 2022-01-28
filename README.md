# Web application for beauty salon management

The aim was to create an application which could allow clients to make appointments and administrators to manage salon's work.

## Technologies:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)

## Installation

Application requires at least Python 3.8 installed. Follow [official documentation](https://www.python.org/downloads/) for more information.
- Go to app root directory - the one where `manage.py` file is
- Create virtual environment - `python3.x -m venv .venv`, where x is installed Python version either 8, 9 or 10
- Activate it - `source .venv/bin/activate/`
- Install dependencies - `pip install -r requirements.txt`
- Create database - `python manage.py makemigrations` and `python manage.py migrate`
- Start app server - `python manage.py runserver`
