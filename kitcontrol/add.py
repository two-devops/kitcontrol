from os.path import exists

from system import System

class AddResources:
    """
    class to add news resources, kits, targets and pipelines

    Methods:
    -------
    add_entity()
    """
    CONFIG_FILE = ".kitcontrol/kitconfig.yaml"

    def __init__(self, system=System()) -> None:
        """
        Args:
            system (obj, optional): class injection. Defaults to System().
        """

        self.system = system

    def add_entity(self, entity_name, name):
        """
        add entity

        Args:
            entity_name (str): (kit, target, pipeline)

            name (str): name
        """

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
