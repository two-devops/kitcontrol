import sys
from click import echo, style

from cmds.system import System
from cmds.config import Config

class Checks:
    """class to check folders and files"""

    def __init__(self) -> None:
        self.config = Config()
        self.system = System()
        # self.kits, self.targets, self.pipelines = self.config.load_config()

    def check_if_exist_folder(self, path):
        """check if exist folder"""
        if not self.system.search(path):
            echo(style(f"\nInfo: {self.file} not found in {self.entity}\n", fg="yellow"))
            sys.exit()

    def check_if_exist_file(self):
        """check if exist file"""
        pass
