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

    def add_entity(self, entity_name, name):
        """
        add entity

        Args:
            entity_name (str): (kit, target, pipeline)

            name (str): name
        """

        sys = System()

        if exists(self.CONFIG_FILE):
            if entity_name == "kit":
                sys.mkdir("kits/" + name)
        else:
            print(f"Error: File {self.CONFIG_FILE} not found")

        return True
