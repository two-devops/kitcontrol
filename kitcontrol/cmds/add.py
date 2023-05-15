from .system import System

class AddResources:
    """Management of entities: kits, targets and pipelines"""

    CONFIG_FILE = ".kitcontrol/config.yaml"

    def __init__(self, system=System()):

        self.system = system

    def add_entity(self, entity_name, name):
        """Create entities; kit, target and pipeline"""

        # Check if config file exist
        if self.system.search(self.CONFIG_FILE):

            # Create Folder and yours config files
            if not self.system.search(entity_name+"s/" + name):
                if entity_name == "kit":
                    self.system.mkdir(entity_name+"s/" + name)
                    self.system.mkfile(entity_name+"s/"+ name, name+".yaml")
                self.system.mkfile(entity_name+"s/", name+".yaml")
            else:
                print(f"Error: directory {entity_name}s/{name} exist")

        else:
            print(f"Error: File {self.CONFIG_FILE} not found")

        return True
