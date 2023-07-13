import sys

from click import prompt, confirm, style

from config.config import Config

from cmds.checks import Checks
from cmds.show import Show
from cmds.system import System

class Secrets:
    """Class to create and management secrets"""

    secrets = ""

    def __init__(self):
        self.check = Checks()
        self.config = Config()
        self.system = System()
        self.config.check_config()
        self.load()
    
    def __checks(self, target):
        """Check targets"""
        self.check.check_if_not_exist(self.config.targets_dir + "/" + target + ".yaml", "not found")
    
    def add(self, target, secret):
        """Add secret"""
        for secr in self.secrets:
            if target in secr:
                print(style(f"\nInfo: target {target} exist\n", fg="yellow"))
                sys.exit()
        self.save(f"{target}={secret}")

    def load(self):
        """Load secret"""
        file = open(self.config.config_folder + "/secrets", "a+", encoding="utf-8")
        file.seek(0)
        try: 
            self.secrets = file.readlines()
        except FileNotFoundError as errors:
            print(errors)
        finally:
            file.close()

    def show(self):
        """Show secret"""
        print(style("Secrets", fg="blue"))
        print(style("-------", fg="blue"))
        for secret in self.secrets:
            print(style(f'{secret}', fg="green"))

    def save(self, secret):
        """Save secret"""
        try: 
            with open(self.config.config_folder + "/secrets", 'a', encoding="utf-8") as file:
                file.write(secret+"\n")
        except FileNotFoundError as errors:
            print(errors)

    def create(self):
        """create secret"""
        secret = prompt("Enter secret", hide_input=True, confirmation_prompt=True)
        Show('targets').show_entity()
        target = prompt("Select Target")
        self.__checks(target)
        self.add(target, secret)
        print(style(f"\nAdd secret:{secret} in target: {target}", fg="green"))
