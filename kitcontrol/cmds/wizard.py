from click import prompt, confirm, echo

from cmds.checks import Checks
from cmds.system import System

from config.config import Config


class Wizard():
    """Interactive creation entities"""

    data = {}

    def __init__(self, entity):
        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.config.check_config()
        # self.kits, self.targets, self.pipelines = self.config.load_config()
        self.wizard()
        
    def wizard(self):   
        """Create entities step by step"""
        if self.entity == "target":
            self.data["name"] = prompt('Please enter name of kit')
            self.data["files"] = prompt('hostname or ip address')
            self.data["values"] = prompt('Enter password', hide_input=True, confirmation_prompt=True)

        if confirm("Do you wan enter other kit"):
            echo("Save new kit")
            self.system.mkfile(self.config.targets_dir, self.entity + self.data["name"], self.data)
            # print(self.data)
        else:
            print(f"{self.entity}", self.data["name"],"not saved")