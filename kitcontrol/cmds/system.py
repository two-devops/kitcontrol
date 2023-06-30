from click import edit
from subprocess import run, PIPE
from os.path import exists

class System:
    """Manage to create folders and files"""

    def command(self, cmd):
        """running commands"""
        return run([cmd], shell=True, stdout=PIPE, check=True, universal_newlines=True, timeout=30)

    def mkfile(self, path, filename, data=None):
        """ Create files"""
        if data:
            config_file = data
        else:
            config_file = ""
        try:
            with open(path + '/' + filename, 'w', encoding="utf-8") as file:
                file.write(config_file)
        except FileNotFoundError as error:
            print(f"Error: {error}")

    def search(self, value):
        """Search field and file"""
        if exists(value):
            return True
        else:
            return False
