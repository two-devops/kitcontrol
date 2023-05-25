import sys

from click import echo, style
from cmds.system import System
from cmds.config import Config

class Show:
    """Class to show kits, targets and pipelines"""

    config = Config()

    def __init__(self, entity, edit=None, system=System()) -> None:

        self.entity = entity
        self.system = system
        self.edit = edit
        self.config.check_config()
        if not self.edit:
            self.show_entity()
        else:
            self.edit_entity()

    def show_entity(self):
        """show kits"""
        values = self.system.mkls(self.entity)
        echo(style(f"\n{self.entity}\n", fg="blue"))
        echo(style(f'{values}', fg='green', italic=True))
    
    def edit_entity(self):
        """edit kits, targets or pipelines"""

        # Check if exits entity
        self.check_exist_entities()

        if self.entity == "kits":
            file = self.entity+"/"+self.edit+"/"+self.edit+".yaml"
        else:
            file = self.entity+"/"+self.edit+".yaml"
        self.system.mkedit(file)

    def check_exist_entities(self):
        """Check exist"""
        if self.entity == "kits":
            if not self.system.search("kits/"+self.edit):
                echo(style(f"\nInfo: {self.edit} not found in {self.entity}\n", fg="yellow"))
                sys.exit()
        else:
            if not self.system.search(self.entity+"/"+self.edit+".yaml"):
                echo(style(f"\nInfo: {self.edit} not found in {self.entity}\n", fg="yellow"))
                sys.exit()
