import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Rename Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name.')
        #parser.add_argument('-p', '--prefix')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']
    
        # a bit of logic to rename the project:
        files_to_rename = [
                'manage.py',
                'demo/settings/components/base.py',
                'demo/wsgi.py',
                'pytest.ini',
            ]

        folder_to_rename = 'demo'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(folder_to_rename, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(f'Project has been renamed to {new_project_name}'))
