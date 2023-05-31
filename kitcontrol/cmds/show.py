from click import echo, style

from cmds.checks import Checks
from cmds.system import System
from cmds.config import Config

class Show:
    """Class to show kits, targets and pipelines"""

    def __init__(self, entity, file=None, system=System()) -> None:

        self.file = file
        self.entity = entity
        self.system = system
        self.config = Config()
        self.check = Checks()
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()
        if not self.file:
            self.show_entity()
        else:
            self.edit_entity()

    def show_entity(self):
        """show kits"""
        if self.entity == "kits":
            values = self.system.ls(self.kits)
        elif self.entity == "targets":
            values = self.system.ls(self.targets)
        else:
            values = self.system.ls(self.pipelines)

        echo(style(f"\n{self.entity}\n", fg="blue"))
        echo(style(f'{values}', fg='green', italic=True))
    
    def edit_entity(self):
        """edit kits, targets or pipelines"""

        if self.entity == "kits":
            self.check.check_if_not_exist(self.kits + "/" + self.file, "not found")
            file = self.kits + "/" + self.file + "/" + self.file+".yaml"
        elif self.entity == "targets":
            self.check.check_if_not_exist(self.targets + "/" + self.file + ".yaml", "not found")
            file = self.targets + "/" + self.file + ".yaml"
        else:
            self.check.check_if_not_exist(self.pipelines + "/" + self.file + ".yaml", "not found")
            file = self.pipelines + "/" + self.file + ".yaml"
        self.system.edit(file)
