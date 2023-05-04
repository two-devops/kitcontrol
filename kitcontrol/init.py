

from system import System

class InitApp:

    """Create the file structure"""

    path = ""
    CONFIG = { "default_config": [{
        "path_kits": "kits",
        "path_targets": "targets",
        "path_pipelines": "pipelines",
        "path_config": ".kitcontrol" }]
    }

    def __init__(self, path, system=System()) -> None:

        self.path = path
        self.system = system

    def build_folders(self):
        """Build folders"""

        for folder in self.CONFIG["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    return False
        return True

    def create_config_files(self, filename):
        """Create config file"""

        path = self.path + "/" + self.CONFIG["default_config"][0]["path_config"]

        result = self.system.mkfile(path, filename, self.CONFIG)

        return result
