from os.path import exists

from system import System

class AddResources:
    """Management of entities: kits, targets and pipelines"""

    CONFIG_FILE = ".kitcontrol/config.yaml"

    def __init__(self, system=System()) -> None:

        self.system = system

    def add_entity(self, entity_name, name):
        """Create entities; kit, target and pipeline"""

        if exists(self.CONFIG_FILE):

            if entity_name == "kit":
                self.system.mkdir("kits/" + name)
                self.system.mkfile("kits/"+ name, name+".yaml")

            if entity_name == "target":
                self.system.mkdir("targets/" + name)
                self.system.mkfile("targets/"+ name, name+".yaml")

            if entity_name == "pipeline":
                self.system.mkdir("pipelines/" + name)
                self.system.mkfile("pipelines/"+ name, name+".yaml")
        else:
            print(f"Error: File {self.CONFIG_FILE} not found")

        return True
