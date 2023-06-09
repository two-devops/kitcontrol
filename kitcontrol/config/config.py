import os

from click import echo, style

from cmds.checks import Checks
from cmds.system import System

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
KITS_DIR = "kits"
TARGETS_DIR = "targets"
PIPELINE_DIR = "pipelines"
CONFIG_FILE = "config.yaml"
CONFIG_KIT = "kit.yaml"
CONFIG_TARGET = "target.yaml"
CONFIG_PIPELINE = "pipeline.yaml"
CONFIG_FOLDER = ".kitcontrol"
CONFIG_PATH = CONFIG_FOLDER + '/' + CONFIG_FILE

class Config:
    """Class to load configs"""
    root_dir = ROOT_DIR + '/'
    kits_dir = KITS_DIR
    targets_dir = TARGETS_DIR
    pipelines_dir = PIPELINE_DIR
    config_file_name = CONFIG_FILE
    config_kit = CONFIG_KIT
    config_target = CONFIG_TARGET
    config_pipeline = CONFIG_PIPELINE
    config_folder = CONFIG_FOLDER
    path_config_file = CONFIG_PATH

    def __init__(self):
        self.check = Checks()
        self.system = System()
        self.config = self._load_config()

    def check_config(self):
        """checking if config file exist"""
        self.check.check_if_not_exist(self.path_config_file, f"\nInfo: There isn't a .kitconfig directory, the {self.path_config_file} not found\n")
    
    def _load_config(self):
        """Load config from .kitcontrol/config.yaml file"""
        if self.system.search(self.path_config_file):
            with open(self.path_config_file, "r", encoding="utf8") as config_file:
                try:
                    data = config_file.read()
                except FileNotFoundError as err:
                    echo(style(f"Info: file {self.config_file_name} - {err}", bg="yellow"))
            return data

    def load_default(self, file):
        """load defaults configs"""
        with open(self.root_dir + file, "r", encoding="utf8") as config_file:
            try:
                data = config_file.read()
            except FileNotFoundError as err:
                echo(style(f"Info: file {self.config_file_name} - {err}", bg="yellow"))
        return data
