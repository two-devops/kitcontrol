from click import echo
import sys
from cmds.system import System

class Config:
    """Class to save configs"""

    NAME_CONFIG_FILE = "config.yaml"
    PATH_CONFIG_FILE = ".kitcontrol/config.yaml"

    KIT_CONTROL_CONFIG = { "default_config": [{
        "path_kits": "kits",
        "path_targets": "targets",
        "path_pipelines": "pipelines",
        "path_config": ".kitcontrol" }]
    }

    def __init__(self, system=System()):
        self.system = system

    def check_config(self):
        """check config file exist"""
        if not self.system.search(self.PATH_CONFIG_FILE):
            echo(f"not a kitconfig directory, the {self.PATH_CONFIG_FILE} not found")
            sys.exit()
