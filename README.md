# Shorten Urls
#### A Django MVC project to short urls .

## Tools :
- Django
- HTML
- Css
- Bootstrap
  

## Installation :
  ### Requirements
  - Python (3.x.x)
  ### SetUp
  - Create virtual environment in Unix , Windows
    ```
    python -m venv venv
    ```
  - Copy project folder to /venv/
    
  - Activate Virtual Environment
    
    Windows
    ```
    /venv/Scripts/activate
    ```
    Unix
    ```
    source /venv/Scripts/activate
    ```
  - Install Requirements
    ```
    cd project
    pip install -r requirements.txt
    ```
  - Create database
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
  - Create Admin User (username,password) required
    ```
    python manage.py createsuperuser
    ```
  - Runserver
    ```
    python manage.py runserver
    ```
