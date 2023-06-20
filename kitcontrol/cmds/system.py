from click import edit
from subprocess import run, PIPE
from os.path import exists

class System:
    """Manage to create folders and files"""

    def mkdir(self, path):
        """ Create fields"""
        return run(["mkdir", "-p", path], capture_output=True, text=True, check=True, timeout=30)

    def ls(self, entity):
        """ Show fields and files"""
        process = run(["ls", "-1", entity], check=True, stdout=PIPE, universal_newlines=True, timeout=30)
        return process.stdout

    def rm(self, entity):
        """ remove fields and files"""
        process = run(["rm", "-rf", entity], check=True, stdout=PIPE, universal_newlines=True, timeout=30)
        return process.stdout

    def cp(self, src_path, dst_path):
        """ copy file in place"""
        return run([f'cp -r {src_path} {dst_path}'], shell=True, check=True)

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

    def edit(self, file):
        """Edit file"""
        edit(filename=file)
