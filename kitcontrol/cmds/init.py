from click import echo, style
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
            echo(f"{self.path} already exist")
            return False

        # Create folders
        for folder in self.config.KIT_CONTROL_CONFIG["default_config"]:
            for directory in folder.values():
                path_folder = self.path + '/' + directory
                if not self.system.mkdir(path_folder):
                    echo(style(f"Error: unknown", fg="red"))
                else:
                    echo(style(f"directory {path_folder} created", fg="green"))

        # Create config file
        path = self.path + "/" + self.config.KIT_CONTROL_CONFIG["default_config"][0]["path_config"]
        self.system.mkfile(path, self.config.NAME_CONFIG_FILE, self.config.KIT_CONTROL_CONFIG_FILE)
