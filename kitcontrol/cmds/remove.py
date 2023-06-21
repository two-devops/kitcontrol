from click import echo, style

from cmds.system import System
from cmds.checks import Checks

from config.config import Config

class Remove():
    """Class to remove fields and files"""

    def __init__(self, entity, file):

        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.file = file
        self.config.check_config()

    def remove(self):
        """remove fields and files"""
        if self.entity == "kit":
            self.check.check_if_not_exist(self.config.kits_dir + "/" + self.file, "not found")
            self.system.command('rm -rf ' + self.config.kits_dir + "/" + self.file)
        elif self.entity == "target":
            self.check.check_if_not_exist(self.config.targets_dir + "/" + self.file + ".yaml", "not found")
            self.system.command('rm -rf ' + self.config.targets_dir + "/" + self.file + ".yaml")
        else:
            self.check.check_if_not_exist(self.config.pipelines_dir + "/" + self.file + ".yaml", "not found")
            self.system.command('rm -rf ' + self.config.pipelines_dir + "/" + self.file + ".yaml")

        echo(style(f"Info: {self.file}.yaml removed", fg="green"))
