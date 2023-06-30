from click import echo, style

from cmds.checks import Checks
from cmds.system import System

from config.config import Config

class Show:
    """Class to show kits, targets and pipelines"""

    def __init__(self, entity):

        self.entity = entity
        self.system = System()
        self.config = Config()
        self.check = Checks()
        self.config.check_config()

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
