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

    def build(self):

        """
        Building folders and create config files for all places
        """

        for folder in self.config["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    return False
        
        return True

        # config_file = yml.safe_dump(self.config)

        # with open(self.path + '/ikctl.yaml', 'w', encoding="utf-8") as file:
        #     file.write(config_file)

        # run(["ls", "-1", self.path], text=True, check=True, timeout=30, stdout=True)
