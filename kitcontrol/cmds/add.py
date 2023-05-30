from click import echo, style

from cmds.checks import Checks
from cmds.system import System
from cmds.config import Config

class Add:
    """Class to create: kits, targets and pipelines"""

    def __init__(self, entity_name, name, system=System()):
        self.entity_name = entity_name
        self.name = name
        self.system = system
        self.check = Checks()
        self.config = Config()
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()
        if self.entity_name == 'kit':
            self.create_kits()
        elif self.entity_name == 'target':
            self.create_targets()
        else:
            self.create_pipelines()

    def create_kits(self):
        """create kits"""
        self.check.check_if_exist(self.kits + "/" + self.name, "already exist")
        self.system.mkdir(self.kits + "/" + self.name)
        self.system.mkfile(self.kits + "/" + self.name, self.name+".yaml", self.config.KIT_CONFIG)
        echo(style(f"Info: create {self.entity_name}: {self.name}.yaml", fg="green"))

    def create_targets(self):
        """create targets"""
        self.check.check_if_exist(self.targets + "/" + self.name+".yaml", "already exist")
        self.system.mkfile(self.targets+"/", self.name+".yaml", self.config.TARGET_CONFIG)
        echo(style(f"Info: create {self.entity_name}: {self.name}.yaml", fg="green"))

    def create_pipelines(self):
        """create pipelines"""
        self.check.check_if_exist(self.pipelines + "/" + self.name+".yaml", "already exist")
        self.system.mkfile(self.pipelines + "/", self.name+".yaml", self.config.PIPELINE_CONFIG)
        echo(style(f"Info: create {self.entity_name}: {self.name}.yaml", fg="green"))
