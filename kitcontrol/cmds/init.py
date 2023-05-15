from cmds.system import System
from cmds.config import Config

class Init:
    """Initiated Application"""

    path = ""

    config = Config()

    def __init__(self, path, system=System()):
        self.path = path
        self.system = system

    def init_app(self):
        """Build folders"""

        # Check if folder exist
        if self.system.search(self.path):
            print(f"Info: directory {self.path} exist")
            return False

        # Create folders
        for folder in self.config.KIT_CONTROL_CONFIG["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    return False

        # Create config file
        path = self.path + "/" + self.config.KIT_CONTROL_CONFIG["default_config"][0]["path_config"]
        self.system.mkfile(path, self.config.CONFIG_FILE, self.config.KIT_CONTROL_CONFIG)
