import sys
import yaml
from yaml.loader import SafeLoader

from click import echo, style
from cmds.system import System

class Config:
    """Class to save configs"""
    NAME_CONFIG_FILE = "config.yaml"
    PATH_CONFIG_FILE = ".kitcontrol/config.yaml"

    KIT_CONTROL_CONFIG = { "default_config": [{
        "path_kits": "kits",
        "path_targets": "targets",
        "path_pipelines": "pipelines",
        "path_config": ".kitcontrol" }],
        "mode":[{
            "type": "normal",
        }]
    }

    KIT_CONTROL_CONFIG_FILE = """---
    default_config:
    - path_config: .kitcontrol
      path_kits: kits
      path_pipelines: pipelines
      path_targets: targets
    mode:
    - type: strict"""

    TARGET_CONFIG = """---
    name: "Docker openssh-server"
    host: localhost
    user: ikcontrol
    port: 2222
    args:
        password: password
        allow_agent: false
        look_for_keys: false
    #   key_filename: '/home/miquel/.ssh/id_rsa_kubernetes-unelink'"""

    PIPELINE_CONFIG = """---
    name: pipeline"""

    KIT_CONFIG = """---
    name: "Hello world kit"

    files: 
    - helloworld.sh

    data: 
        worldof: Two-devops"""

    def __init__(self, system=System()):
        self.system = system

    def check_config(self):
        """checking if config file exist"""
        if not self.system.search(self.PATH_CONFIG_FILE):
            echo(style(f"\nInfo: There isn't a .kitconfig directory, the {self.PATH_CONFIG_FILE} not found\n", fg="yellow"))
            sys.exit()

    def load_config(self):
        """load .kitconfig/config.yaml"""
        # self.check_config()
        with open(self.PATH_CONFIG_FILE, "r", encoding="utf8") as config_file:
            try:
                data = yaml.load(config_file, Loader=SafeLoader)
            except yaml.YAMLError as err:
                echo(f"{err}")
        kit = data["default_config"][0]["path_kits"]
        target = data["default_config"][0]["path_targets"]
        pipeline = data["default_config"][0]["path_pipelines"]

        return kit, target, pipeline
