from click import echo, style

from cmds.checks import Checks
from cmds.system import System
from cmds.config import Config

class Add:
    """Class to create: kits, targets and pipelines"""

    def __init__(self, entity, file):

        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.file = file
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()

    def create(self):
        """create kits, targets and pipelines"""
        if self.entity == "kit":
            self.check.check_if_exist(self.kits + "/" + self.file, "already exist")
            self.system.mkdir(self.kits + "/" + self.file)
            self.system.mkfile(self.kits + "/" + self.file, self.file+".yaml", self.config.KIT_CONFIG)
        elif self.entity == "target":
            self.check.check_if_exist(self.targets + "/" + self.file+".yaml", "already exist")
            self.system.mkfile(self.targets+"/", self.file+".yaml", self.config.TARGET_CONFIG)
        else: 
            self.check.check_if_exist(self.pipelines + "/" + self.file+".yaml", "already exist")
            self.system.mkfile(self.pipelines + "/", self.file+".yaml", self.config.PIPELINE_CONFIG)

        echo(style(f"Info: create {self.entity}: {self.file}.yaml", fg="green"))
