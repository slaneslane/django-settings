"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:

For production environment:
`DJANGO_ENV=production python manage.py runserver`

For testing environment:
`DJANGO_ENV=test pytest`

Or export environmental variable like this:
export DJANGO_ENV=test
and then use testing environment without setting DJANGO_ENV by every pytest command.
"""

from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/base.py',  # standard django settings
    'components/database.py',
    'components/ldap.py',
    'components/logs.py',

    # Select the right env:
    f'environments/{ENV}.py',
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
