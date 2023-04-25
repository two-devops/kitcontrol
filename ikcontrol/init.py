import yaml as yml

from system import System

class InitApp:

    """
    Class to build folders needed to running app ikctl

    Attributes:
    ----------
    path =  str
    config = dict


    Methods:
    -------
    """
    path = ""
    config = { "default_config": [{
                "path_kits": "kits",
                "path_targets": "targets",
                "path_pipelines": "pipelines" }]}


    def __init__(self, path, system=System()) -> None:

        """
        Save path to self.path

        Args:
            path (_str_): path
        """

        self.path = path
        self.system = system


    def build_folders(self):
        """
        Building folders 
        """

        for folder in self.config["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    return False
        return True


    def create_config_files(self):
        """and create config files for all places
        """
        config_file = yml.safe_dump(self.config)

        result = self.system.create_file(self.path, config_file)

        return result
