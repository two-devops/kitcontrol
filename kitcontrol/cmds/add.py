from cmds.system import System
from cmds.config import Config

class Add:
    """Management of entities: kits, targets and pipelines"""

    config = Config()

    def __init__(self, system=System()):

        self.system = system
        self.config.check_config()

    def add_entity(self, entity_name, name):
        """Create entities; kit, target and pipeline"""

        # Create Folder and yours config files
        if not self.system.search(entity_name+"s/" + name):
            if entity_name == "kit":
                self.system.mkdir(entity_name+"s/" + name)
                self.system.mkfile(entity_name+"s/"+ name, name+".yaml")
            else:
                self.system.mkfile(entity_name+"s/", name+".yaml")
        else:
            print(f"Info: directory {entity_name}s/{name} exist")

        return True
