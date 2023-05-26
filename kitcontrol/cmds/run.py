import sys
from click import echo, style
from cmds.system import System
from cmds.config import Config
from core.pipeline import Pipeline

class Run:
    """Class to exec kits, targets and pipelines"""

    config = Config()

    def __init__(self, kit, target, pipeline=None, sudo=None, system=System()):
        self.kit = kit
        self.target = target
        self.pipeline = pipeline
        self.sudo = sudo
        self.system = system
        self.config.check_config()
        self.check_exist_entities()

    def run(self):
        """exec kits"""
        pipeline = Pipeline(kit=self.kit, target=self.target)
        pipeline.run()

    def check_exist_entities(self):
        """Check exist"""
        if not self.system.search(self.config.path_kits + "/" + self.kit):
            echo(style(f"\nInfo: kit {self.kit} not found\n", fg="yellow"))
            sys.exit()

        if not self.system.search(self.config.path_targets + "/" + self.target+".yaml"):
            echo(style(f"\nInfo: target {self.target} not found\n", fg="yellow"))
            sys.exit()
