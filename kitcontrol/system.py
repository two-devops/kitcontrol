from subprocess import run

import yaml as yml


class System:
    '''
    Manage to create folders and files
    '''
    def mkdir(self, path):
        ''' 
        Create fields
        ''' 
        print(path)
        return run(["mkdir", "-p", path], capture_output=True, text=True, check=True, timeout=30)

    def mkfile(self, path, filename, data=None):
        ''' 
        Create files
        '''
        if data:
            config_file = yml.safe_dump(data)
        else:
            config_file = ""

        try:
            with open(path + '/' + filename, 'w', encoding="utf-8") as file:
                file.write(config_file)
        except Exception as error:
            print("Error:", error)
