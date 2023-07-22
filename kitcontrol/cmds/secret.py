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
    
    def load(self):
        """Load secret"""
        file = open(self.config.config_folder + "/secrets.env", "a+", encoding="utf-8")
        file.seek(0)
        try: 
            self.secrets = file.readlines()
        except FileNotFoundError as errors:
            print(errors)
        finally:
            file.close()

    def add(self, target, secret, action="add"):
        """Add secret"""
        for index, value in enumerate(self.secrets):
            if target in value and "add" in action:
                print(style(f"\nInfo: target {target} exist\n", fg="yellow"))
                sys.exit()
            elif target in value and "update" in action: 
                self.secrets[index] = target+"="+secret+"\n"
        if "add" in action: 
            self.secrets.append(target+"="+secret+"\n")
        self.save(self.secrets)
    
    def save(self, secret):
        """Save secret"""
        try: 
            with open(self.config.config_folder + "/secrets.env", 'w', encoding="utf-8") as file:
                file.writelines(secret)
        except FileNotFoundError as errors:
            print(errors)

    def delete(self, secret):
        """Delete secret""" 
        for index, value in enumerate(self.secrets):
            if secret in value:
                self.secrets.pop(index)
        self.save(self.secrets)

    def create(self):
        """create secret"""
        secret = prompt("Enter secret", hide_input=True, confirmation_prompt=True)
        Show('targets').show_entity()
        target = prompt("Select Target")
        self.__checks(target)
        self.add(target, secret)
        print(style(f"\nAdd secret:{secret} in target: {target}", fg="green"))

    def show(self):
        """Show secret"""
        print()
        print(style("Secrets", fg="blue"))
        print(style("#######", fg="blue"))
        print("--------")
        for secret in self.secrets:
            print(style(secret.replace("\n", ""), fg="green"))
            print("--------")
    
    def update(self):
        """Update passwords"""
        self.show()
        target = prompt("Select target")
        secret = prompt("Enter secret", hide_input=True, confirmation_prompt=True)
        self.__checks(target)
        self.add(target, secret, "update")
        print(style(f"\nUpdate secret: {secret} in target: {target}", fg="green"))

    def remove(self):
        """Delete passwords"""
        self.show()
        target = prompt("Select target to delete")
        self.__checks(target)
        self.delete(target)
        print(style(f"\nDelete target: {target}", fg="green"))