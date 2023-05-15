from cmds.system import System
from cmds.config import Config
from core.pipeline import Pipeline

class Run:
    """Class to exec kits, targets and pipelines"""

    def __init__(self, kit, target, pipeline=None, system=System()):
        self.kit = kit
        self.target = target
        self.pipeline = pipeline
        self.system = system

    def run(self):
        """exec kits"""
        ## To Do: refactor how to instanciator System() and Config()
        config = Config()
        if  self.system.search(config.CONFIG_FILE):
            pipeline = Pipeline(kit=self.kit, target=self.target)
            pipeline.run()
        else:
            print(".kitcontrol folder not found")
