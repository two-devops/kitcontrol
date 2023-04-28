import os
import yaml as yml

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
    temporal_config = {
        "abpath": "kitcontrol_abpath"
    }
    config = { "default_config": [{
            "path_kits": "kits",
            "path_targets": "targets",
            "path_pipelines": "pipelines" }]
        }

    def __init__(self, path, system=System()) -> None:

        """
        Args:
            path (_str_):
            filename (_str_): 
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
        # Create temporal file
        basepath = os.path.abspath(self.path)
        self.system.tmp_files(self.temporal_config["abpath"], basepath)

        return True


    def create_config_files(self, filename):
        """
        Create config files for all places
        """
        config_file = yml.safe_dump(self.config)

        result = self.system.create_file(self.path, filename, config_file)

        return result
