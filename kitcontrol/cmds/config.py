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
    name: "Test kit to explore possibilities"

    # Extensions:

    # .sh -> render and run with "bash xxx.sh"
    # .py -> render and run with "python xxx.py"

    # .others -> only upload

    files:
    - install-tdagent.sh
    - tdagent.*

    # If find a folder with distro name, upload all files inside
    # - /debian

    # Distro-based files INSIDE /distro folder
    # Ex: /debian/install-tdagent.sh

    # executable files can be prefixed with distro. Ex: debian-install-tdagent.sh
    - public.key
    - install-key.sh
    - add-sudoers.py
    - install-tdagent.sh

    # Key-distro specific files:
    - ['debian']:
        - docker.deb
    
    - ['redhat']:
        - docker.rpm


    ## Returns dict with filename: contents or filepath

    ## Ex:
    # { 
    # 'public.key': './public.key', 
    # 'install-key.sh': 'renderer contents in string.....',
    # 'add-sudoers.py': 'renderer contents in string.....',
    # }

    data: 
    # Data first-level (common)
    worldof: "world of bash"

    '[install-key.sh]':
        # Second-level (key with file name)
        worldof: "World of python"


    '[add-sudoers.py]':
        # Second-level (key with file name)
        worldof: "World of python"""

    def __init__(self, system=System()):
        self.system = system
        self.path_folders = self.load_config()
        self.path_kits = self.path_folders["default_config"][0]["path_kits"]
        self.path_targets = self.path_folders["default_config"][0]["path_targets"]
        self.path_pipelines = self.path_folders["default_config"][0]["path_pipelines"]

    def check_config(self):
        """checking if config file exist"""
        if not self.system.search(self.PATH_CONFIG_FILE):
            echo(style(f"\nInfo: There isn't a .kitconfig directory, the {self.PATH_CONFIG_FILE} not found\n", fg="yellow"))
            sys.exit()

    def load_config(self):
        """load .kitconfig/config.yaml"""
        self.check_config()
        with open(self.PATH_CONFIG_FILE, "r", encoding="utf8") as config_file:
            try:
                data = yaml.load(config_file, Loader=SafeLoader)
            except yaml.YAMLError as err:
                echo(f"{err}")
        return data
