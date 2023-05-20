from click import echo, style
from cmds.system import System
from cmds.config import Config

class Show:
    """Class to show kits, targets and pipelines"""

    config = Config()

    def __init__(self, entity, system=System()) -> None:

        self.entity = entity
        self.system = system
        self.config.check_config()

    def show_entity(self):
        """show kits"""

        values = self.system.mkls(self.entity)
        echo(style(f"\n{self.entity}\n", fg="blue"))
        echo(style(f'{values}', fg='green', italic=True))
