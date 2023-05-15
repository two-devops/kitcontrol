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

    def run(self):
        """exec kits"""
        if  self.system.search(self.config.CONFIG_FILE):
            pipeline = Pipeline(kit=self.kit, target=self.target)
            pipeline.run()
        else:
            print(f"Info: File {self.config.PATH_CONFIG_FILE} not found")
