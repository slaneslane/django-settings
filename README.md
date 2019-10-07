After cloning this project, to customize where the virtualenv shoule be created,
add .venv file with the path to virtualenv in project directory.

If You want to use exact python version (not the default one) use first:

    pipenv --python c:\Python36-32\python.exe


Install environment and its requirements with following command (you must have pipenv installed):

    pipenv install --dev

or for production only:

    pipenv install


To get into virtualenv:

    pipenv shell

To run django commands from outside of virtualenv:

    pipenv run python manage.py runserver

To exit virtualenv:

    exit

