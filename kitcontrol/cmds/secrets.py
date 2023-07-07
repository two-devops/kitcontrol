import sys

from click import prompt, confirm, style

from config.config import Config

from cmds.checks import Checks
from cmds.show import Show
from cmds.system import System

class Secrets:
    """Class to create and management secrets"""

    def __init__(self):
        self.check = Checks()
        self.config = Config()
        self.system = System()
        self.config.check_config()

    def __checks(self, target):
        """Check targets"""
        self.check.check_if_not_exist(self.config.targets_dir + "/" + target + ".yaml", "not found")
    
    def save_secret(self, target, secret):
        """Load file secrets or to create it""" 
        if not self.system.search(self.config.config_folder + "/secrets"):
            file = open(self.config.config_folder + "/secrets", 'w', encoding="utf-8")
            file.close()
        else:
            with open(self.config.config_folder + "/secrets", 'r', encoding="utf-8") as file:
                # lines = file.readlines()
                for line in file:
                    if target in line:
                        print(style(f"\nInfo: target {target} exist\n", fg="yellow"))
                        sys.exit()

        if self.system.search(self.config.config_folder + "/secrets"):
            with open(self.config.config_folder + "/secrets", 'a', encoding="utf-8") as file:
                file.write(f"{target}:{secret}\n")

    def create(self):
        """create secret"""
        secret = prompt("Enter secret", hide_input=True, confirmation_prompt=True)
        Show('targets').show_entity()
        target = prompt("Select Target")
        self.__checks(target)
        self.save_secret(target, secret)
        print(style(f"\nAdd secret:{secret} in target: {target}", fg="green"))
    
    def show_secrets(self):
        """Show secrets"""
        with open(self.config.config_folder + "/secrets", 'r', encoding="utf-8") as file:
            print(style("Secrets", fg="blue"))
            print(style("-------", fg="blue"))
            for line in file:
                print(style(f'{line}', fg="green"))
            
            