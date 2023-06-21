from click import echo, style

from cmds.checks import Checks
from cmds.system import System

from config.config import Config

class Show:
    """Class to show kits, targets and pipelines"""

    def __init__(self, entity, file=None) -> None:

        self.file = file
        self.entity = entity
        self.system = System()
        self.config = Config()
        self.check = Checks()
        self.config.check_config()
        if not self.file:
            self.show_entity()
        else:
            self.edit_entity()

    def show_entity(self):
        """show kits, targets and pipelines"""
        if self.entity == "kits":
            values = self.system.command('ls -1 ' + self.config.kits_dir)
        elif self.entity == "targets":
            values = self.system.command('ls -1 ' + self.config.targets_dir)
        else:
            values = self.system.command('ls -1 ' + self.config.pipelines_dir)
        echo(style(f"\n{self.entity}\n", fg="blue"))
        echo(style(f'{values.stdout}', fg='green', italic=True))

    def edit_entity(self):
        """edit kits, targets or pipelines"""
        if self.entity == "kits":
            self.check.check_if_not_exist(self.config.kits_dir + "/" + self.file, "not found")
            file = self.config.kits_dir + "/" + self.file + "/" + self.file + ".yaml"
        elif self.entity == "targets":
            self.check.check_if_not_exist(self.config.targets_dir + "/" + self.file + ".yaml", "not found")
            file = self.config.targets_dir + "/" + self.file + ".yaml"
        else:
            self.check.check_if_not_exist(self.config.pipelines_dir + "/" + self.file + ".yaml", "not found")
            file = self.config.pipelines_dir + "/" + self.file + ".yaml"
        self.system.edit(file)
