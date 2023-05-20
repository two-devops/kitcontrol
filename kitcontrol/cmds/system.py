from subprocess import run, PIPE
from os.path import exists

import yaml as yml

class System:
    """Manage to create folders and files"""

    def mkdir(self, path):
        """ Create fields"""
        try:
            return run(["mkdir", "-p", path], capture_output=True, text=True, check=True, timeout=30)
        except FileExistsError as err:
            print(err)

    def mkls(self, entity):
        """ Show fields and files"""
        try:
            process = run(["ls", "-1", entity], check=True, stdout=PIPE, universal_newlines=True, timeout=30)
            return process.stdout
        except FileNotFoundError as err:
            print(err)

    def mkfile(self, path, filename, data=None):
        """ Create files"""
        if data:
            config_file = yml.safe_dump(data)
        else:
            config_file = ""
        try:
            with open(path + '/' + filename, 'w', encoding="utf-8") as file:
                file.write(config_file)
        except Exception as error:
            print(f"Error: {error}")

    def search(self, value):
        """Search field and file"""
        if exists(value):
            return True
        else:
            return False
