from click import prompt, confirm, echo

from cmds.checks import Checks
from cmds.system import System
from cmds.config import Config


class Wizard():
    """Interactive creation entities"""

    data = {}

    def __init__(self, entity):

        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()
        self.wizard()
        
       
    def wizard(self):   
        """Create entities step by step"""
        while True:
            if self.entity == "kit":
                self.data['name'] = prompt('Please enter name of kit')
                self.data["files"] = prompt('Enter files names')
                self.data["values"] = prompt('Enter key values for kti')

            if not confirm("Do you wan enter other kit"): 
                echo("Save new kit")
                break

        print(self.data)

