from subprocess import run

class System:
    """Class System
    """

    def mkdir(self, path):
        """To create fields

        Args:
            path (_type_): path where we want create fields

        Returns:
            _type_: bool
        """
        print(path)
        return run(["mkdir", "-p", path], capture_output=True, text=True, check=True, timeout=30)

    def create_file(self, path, data=None):
        """Create config files 

        Args:
            data (_type_, optional): _str_. Defaults to None.
        """
        with open(path + '/kitctl.yaml', 'w', encoding="utf-8") as file:
            file.write(data)

        with open(path + '/kitctl.yaml', 'r', encoding="utf-8") as file:
            result = file.read()
        return result
