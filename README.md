# Django Polls Application
Django-polls is a basic poll application which consist of two parts: a public site and admin site. A public site allows users to vote or track the results in the webpage. An admin site is for adding, changing, and deleting poll questions. [source](https://docs.djangoproject.com/en/2.2/intro/)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
## Prerequisites
The application requires:
- [Python](https://www.python.org/) 3.6 or newer
- [Django](https://docs.djangoproject.com/en/2.2/topics/install/) 2.1.2 or newer
- Python add-on modules as in [requirements.txt](requirements.txt)




## Installing 
### Step 1: Clone repository
    git clone https://github.com/bameethanida/django-polls.git

### Step 2: Go to django-polls directory
    cd django-polls

### Step 3: Install all dependencies and run database migrations.
On MacOS and Linux:

    pip3 install -r requirements.txt

    python3 manage.py migrate

On Windows:

    pip install -r requirements.txt

    py manage.py migrate


## Running the tests

### Step 1: Open terminal
    cd django-poll/mysite
### Step 2: Run server

On MacOS and Linux:   

    python3 manage.py runserver  

On Windows:

    py manage.py runserver


## Author
Thanida Jongarnon 6110545538
