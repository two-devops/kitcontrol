

from system import System

class InitApp:

    """
    Class to build folders

    Attributes:
    ----------
    path =  str
    config = dict


    Methods:
    -------
    build_folders
    create_config_files
    """


    path = ""
    CONFIG = { "default_config": [{
        "path_kits": "kits",
        "path_targets": "targets",
        "path_pipelines": "pipelines",
        "path_config": ".kitcontrol" }]
    }

    def __init__(self, path, system=System()) -> None:
        """
        Args:
            path (_str_):
            system (obj, optional): class injection. Defaults to System().
        """

        self.path = path
        self.system = system

    def build_folders(self):
        """
        Building folders 
        """
        for folder in self.CONFIG["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    return False

        return True


    def create_config_files(self, filename):
        """
        Create config kitcontrol.yaml
        """

        path = self.path + "/" + self.CONFIG["default_config"][0]["path_config"]

        result = self.system.mkfile(path, filename, self.CONFIG)

        return result
