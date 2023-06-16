import yaml

from click import prompt, confirm, echo, style
from yaml.loader import SafeLoader

from cmds.checks import Checks
from cmds.system import System

from config.config import Config


class Wizard():
    """Interactive creation entities"""

    data = {}

    def __init__(self, entity, file):
        self.config = Config()
        self.system = System()
        self.check = Checks()
        self.entity = entity
        self.file = file
        self.config.check_config()
        self.kit = self.open_default_config(self.config.config_kit)
        self.target = self.open_default_config(self.config.config_target)
        self.pipeline = self.open_default_config(self.config.config_pipeline)
        self.wizard()
        
    def wizard(self):   
        """Create entities step by step"""
        if self.entity == "kit":
            directory = self.config.kits_dir
            self.data = self.kit
            self.data["name"] = prompt('Name', default=self.file)

        if self.entity == "target":
            directory = self.config.targets_dir
            self.data = self.target
            self.data["name"] = prompt('Name', default=self.file)
            self.data["host"] = prompt('Hostname or ip address', default="127.0.0.1")
            self.data["user"] = prompt('User', default="user")
            self.data["port"] = prompt('Port', default=22)
            self.data["args"]["password"] = prompt('Enter password', hide_input=True, confirmation_prompt=True)
            self.data["args"]["allow_agent"] = prompt('Allow Agent', default=False)
            self.data["args"]["look_for_keys"] = prompt('Look for Keys', default=False)

        if self.entity == "pipeline":
            directory = self.config.pipelines_dir
            self.data = self.pipeline
            self.data["name"] = prompt('Name', default=self.file)

        if confirm(f"Do you want save {self.data['name']}?"):
            data = yaml.dump(self.data, default_flow_style=False)
            if self.entity == "kit":
                self.check.check_if_exist(directory + "/" + self.data["name"] + "/" + self.data["name"]+".yaml", "already exist, try again with other name")
                self.system.mkdir(directory + "/" + self.data["name"])
                self.system.mkfile(directory + "/" + self.data["name"], self.data["name"]+'.yaml', data)
            else: 
                self.check.check_if_exist(directory + "/" + self.data["name"]+".yaml", "already exist, try again with other name")
                self.system.mkfile(directory, self.data["name"]+'.yaml', data)
            echo(f"The {self.entity} {self.data['name']} saved correctly")
        else:
            echo(f"{self.entity} {self.data['name']} not saved")
    
    def open_default_config(self, file):
        """Open default config and transform to dict"""
        data = self.config.load_default(file)
        data = yaml.load(data, Loader=SafeLoader)
        return data
