import sys
from click import echo
from cmds.system import System
from cmds.config import Config
from core.pipeline import Pipeline

class Run:
    """Class to exec kits, targets and pipelines"""

    config = Config()

    def __init__(self, kit, target, pipeline=None, system=System()):
        self.kit = kit
        self.target = target
        self.pipeline = pipeline
        self.system = system
        self.config.check_config()
        self.check_exist_entities()

    def run(self):
        """exec kits"""
        pipeline = Pipeline(kit=self.kit, target=self.target)
        pipeline.run()

    def check_exist_entities(self):
        """Check exist"""
        if not self.system.search("kits/"+self.kit):
            echo("kit not found")
            sys.exit()

        if not self.system.search("targets/"+self.target+".yaml"):
            echo("target not found")
            sys.exit()
