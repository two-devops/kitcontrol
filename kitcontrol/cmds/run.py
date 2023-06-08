from cmds.checks import Checks

from config.config import Config

from core.pipeline import Pipeline

class Run:
    """Class to exec kits, targets and pipelines"""

    def __init__(self, kit, target, pipeline=None, sudo=None):
        self.kit = kit
        self.target = target
        self.pipeline = pipeline
        self.sudo = sudo
        self.config = Config()
        self.check = Checks()
        self.config.check_config()
        self.check.check_if_not_exist(self.config.kits_dir + "/" + self.kit, "not found")
        self.check.check_if_not_exist(self.config.targets_dir + "/" + self.target + ".yaml", "not found")

    def run(self):
        """exec kits"""
        pipeline = Pipeline(kit=self.kit, target=self.target)
        pipeline.run()
