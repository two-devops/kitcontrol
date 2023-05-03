from subprocess import run

import yaml as yml


class System:
    """
    Class System
    """

    def mkdir(self, path):
        """
        Create fields

        Args:
            path (_type_): path where we want create fields

        Returns:
            _type_: bool
        """
        print(path)
        return run(["mkdir", "-p", path], capture_output=True, text=True, check=True, timeout=30)

    def mkfile(self, path, filename, data=None):
        """
        Args:
            data (_type_, optional) 

        Returns:
            _type_: str
        """
        if data:
            config_file = yml.safe_dump(data)
        else:
            config_file = ""

        try:
            with open(path + '/' + filename, 'w', encoding="utf-8") as file:
                file.write(config_file)
        except Exception as error:
            print("Error:", error)

        try:
            with open(path + '/' + filename, 'r', encoding="utf-8") as file:
                result = file.read()
            return result
        except Exception as error:
            print("Error:", error)
