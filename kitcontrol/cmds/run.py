from click import prompt, confirm, echo, style

from cmds.checks import Checks
from cmds.show import Show

from config.config import Config

from core.pipeline import Pipeline

class Run:
    """Class to exec kits, targets and pipelines"""


    def __init__(self, kit=None, target=None, pipeline=None, sudo=None):
        self.kit = kit
        self.target = target
        self.pipeline = pipeline
        self.sudo = sudo
        self.config = Config()
        self.check = Checks()
        self.config.check_config()

    def __checks(self):
        """check entities"""
        if self.kit:
            self.check.check_if_not_exist(self.config.kits_dir + "/" + self.kit, "not found")
        if self.target:
            self.check.check_if_not_exist(self.config.targets_dir + "/" + self.target + ".yaml", "not found")

    def run_interactive(self):
        """interactive run"""
        Show('kits').show_entity()
        self.kit = prompt('Enter kit')
        Show('targets').show_entity()
        self.target = prompt('Enter target')
        self.__checks()
        self.run()

    def run(self):
        """exec kits"""
        if self.pipeline:
            pipeline = Pipeline(self.pipeline)
            pipeline.start()
        else: 
            self.__checks()
            pipeline = Pipeline(kit=self.kit, target=self.target)
            pipeline.run()
