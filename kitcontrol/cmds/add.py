from click import echo, style

from cmds.checks import Checks
from cmds.system import System
from cmds.wizard import Wizard

from config.config import Config

class Add:
    """Class to create: kits, targets and pipelines"""

    def __init__(self, entity, file, wizard=None):

        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.file = file
        self.wizard = wizard
        self.config.check_config()
        if self.wizard:
            Wizard(entity, file)
        else:
            self.create()

    def create(self):
        """create kits, targets and pipelines"""
        if self.entity == "kit":
            self.check.check_if_exist(self.config.kits_dir + "/" + self.file, "already exist")
            self.system.command('mkdir -p ' + self.config.kits_dir + "/" + self.file)
            self.system.mkfile(self.config.kits_dir + "/" + self.file, self.file+".yaml", self.config.load_default(self.config.config_kit))
        elif self.entity == "target":
            self.check.check_if_exist(self.config.targets_dir + "/" + self.file+".yaml", "already exist")
            self.system.mkfile(self.config.targets_dir+"/", self.file+".yaml", self.config.load_default(self.config.config_target))
        else: 
            self.check.check_if_exist(self.config.pipelines_dir + "/" + self.file+".yaml", "already exist")
            self.system.mkfile(self.config.pipelines_dir + "/", self.file+".yaml", self.config.load_default(self.config.config_pipeline))

        echo(style(f"Info: create {self.entity}: {self.file}.yaml", fg="green"))
