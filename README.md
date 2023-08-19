# xnara
 An api webhook for retreving data from 2 other endpoints and combining them in format and give the required payload
Note :for logging check file named 'log' in the main app folder.Wanted to use APM for all logs but due to shortage of time avoided it.
 
# Table of Contents

- [Installation](#installation)
- [Run APP](#runapp)
- [API](#api)

# Installation
- Install virtualenv
  - pip<version> install virtualenv
    eg. pip3 install virtualenv
- Create Virtual Env
  - python<version> -m venv <virtual-environment-name>
    eg: python3 -m venv env
- Activate Env
  - source <virtual-environment-name>/bin/activate
    eg: source env/bin/activate
  - pip install -r requirements.txt

## Run APP
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver

## API
- http://localhost:8000/webhook/packed_data (method-GET)
}
