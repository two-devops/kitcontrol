from click import echo, style

from cmds.system import System
from cmds.config import Config
from cmds.checks import Checks

class Remove():
    """Class to remove fields and files"""

    def __init__(self, entity, file):

        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.file = file
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()

    def remove(self):
        """remove fields and files"""
        if self.entity == "kit":
            self.check.check_if_not_exist(self.kits + "/" + self.file, "not found")
            self.system.rm(self.kits + "/" + self.file)
        elif self.entity == "target":
            self.check.check_if_not_exist(self.targets + "/" + self.file + ".yaml", "not found")
            self.system.rm(self.targets + "/" + self.file + ".yaml")
        else:
            self.check.check_if_not_exist(self.pipelines + "/" + self.file + ".yaml", "not found")
            self.system.rm(self.pipelines + "/" + self.file + ".yaml")

        echo(style(f"Info: {self.file}.yaml removed", fg="green"))
