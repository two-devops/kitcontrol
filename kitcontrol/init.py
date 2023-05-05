from system import System

class InitApp:

    """Initiated Application"""

    path = ""

    CONFIG = { "default_config": [{
        "path_kits": "kits",
        "path_targets": "targets",
        "path_pipelines": "pipelines",
        "path_config": ".kitcontrol" }]
    }

    CONFIG_NAME = "config.yaml"

    def __init__(self, path, system=System()) -> None:

        self.path = path
        self.system = system

    def init_app(self):
        """Build folders"""

        for folder in self.CONFIG["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    return False

        path = self.path + "/" + self.CONFIG["default_config"][0]["path_config"]

        result = self.system.mkfile(path, self.CONFIG_NAME, self.CONFIG)

        return result
