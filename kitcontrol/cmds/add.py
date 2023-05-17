from click import echo
from cmds.system import System
from cmds.config import Config

class Add:
    """Management of entities: kits, targets and pipelines"""

    config = Config()

    def __init__(self, entity_name, name, system=System()):

        self.entity_name = entity_name
        self.name = name
        self.system = system
        self.config.check_config()
    
    def add_entity(self):
        """create entities"""
        if self.entity_name == 'kit':
            self.create_kits()
        else:
            self.create_targets_or_pipelines()

    def create_kits(self):
        """create kits"""

        if not self.system.search(self.entity_name+"s/" + self.name):
            self.system.mkdir(self.entity_name+"s/" + self.name)
            self.system.mkfile(self.entity_name+"s/"+ self.name, self.name+".yaml")
            echo(f"create {self.entity_name}: {self.name}.yaml")
        else:
            echo(f"{self.entity_name} {self.name}.yaml already exist")

    def create_targets_or_pipelines(self):
        """create targets or pipelines"""

        if not self.system.search(self.entity_name+"s/" + self.name + ".yaml"):
            self.system.mkfile(self.entity_name+"s/", self.name+".yaml")
            echo(f"create {self.entity_name}: {self.name}.yaml")
        else:
            echo(f"{self.entity_name} {self.name}.yaml already exist")
