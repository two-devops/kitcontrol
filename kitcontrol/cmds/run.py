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

    def run(self):
        """exec kits"""
        pipeline = Pipeline(kit=self.kit, target=self.target)
        pipeline.run()
