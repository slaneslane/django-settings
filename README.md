After cloning this project, to customize where the virtualenv shoule be created,
add .venv file with the path to virtualenv in project directory.

If You want to use exact python version (not the default one) use first:

    pipenv --python c:\Python36-32\python.exe


Install environment and its requirements with following command (you must have pipenv installed):

    pipenv install --dev

or for production only:

    pipenv install


To run django commands from outside of virtualenv (development environment as default):
[django extensions is installed in development environment only]

    pipenv run python manage.py runserver_plus

To get into virtualenv:

    pipenv shell


To run server in production environment from inside of virtualenv:
[django extensions command runserver_plus is not available in production environment]

    DJANGO_ENV=production python manage.py runserver

or:
    
    export DJANGO_ENV=production
    python manage.py runserver
    

To run test environment from inside of virtualenv:
[django extensions command runserver_plus is not available in test environment]
[special django test settings are available, like installed test related app: dummy_app]

    DJANGO_ENV=test ptw 

or:
    
    export DJANGO_ENV=test
    pytest -v
    

To exit virtualenv:

    exit

