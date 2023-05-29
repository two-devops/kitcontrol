from click import echo, style
from cmds.system import System
from cmds.config import Config

class Add:
    """Class to create: kits, targets and pipelines"""

    config = Config()

    def __init__(self, entity_name, name, system=System()):
        self.entity_name = entity_name
        self.name = name
        self.system = system
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()
        print(self.kits)
        print(self.targets)
        print(self.pipelines)
        if self.entity_name == 'kits':
            self.create_kits()
        elif self.entity_name == 'targets':
            self.create_targets()
        else:
            self.create_pipelines()

    def create_kits(self):
        """create kits"""
        if not self.system.search(self.kits + "/" + self.name):
            self.system.mkdir(self.kits + "/" + self.name)
            self.system.mkfile(self.kits + "/" + self.name, self.name+".yaml", self.config.KIT_CONFIG)
            echo(style(f"Info: create {self.entity_name}: {self.name}.yaml", fg="green"))
        else:
            echo(style(f"Warn: {self.entity_name} {self.name}.yaml already exist", fg="yellow"))

    def create_targets(self):
        """create targets"""
        if not self.system.search(self.targets + "/" + self.name + ".yaml"):
            self.system.mkfile(self.targets+"/", self.name+".yaml", self.config.TARGET_CONFIG)
            echo(style(f"Info: create {self.entity_name}: {self.name}.yaml", fg="green"))
        else:
            echo(style(f"Warn: {self.entity_name} {self.name}.yaml already exist", fg="yellow"))

    def create_pipelines(self):
        """create pipelines"""
        if not self.system.search(self.pipelines + "/" + self.name + ".yaml"):
            self.system.mkfile(self.pipelines + "/", self.name+".yaml", self.config.PIPELINE_CONFIG)
            echo(style(f"Info: create {self.entity_name}: {self.name}.yaml", fg="green"))
        else:
            echo(style(f"Warn: {self.entity_name} {self.name}.yaml already exist", fg="yellow"))
