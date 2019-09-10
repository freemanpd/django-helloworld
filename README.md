# django-helloworld
An example Django ["Hello World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) application.

## Screenshots

## Requirements
1. Python 3.4+
1. Pipenv 

## Installation
1. Start Python virtual ENV
```
pipenv shell
```
2. Install dependencies
```
pipenv install
```
3. Run database migrations
```
python3 manage.py migrate
```
4. Create admin user
```
python manage.py createsuperuser --username admin
```

## Run application
```
python manage.py runserver
```
Once the server is running, visit http://127.0.0.1:8000 in your web browser. Now, you should see something like the following:

## Resources
* Properly installing Python - https://docs.python-guide.org/starting/installation/
* Pipenv and virtual environments - https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref