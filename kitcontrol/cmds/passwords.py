import sys

from re import findall, sub

from click import prompt, style

from config.config import Config

from cmds.checks import Checks
from cmds.show import Show
from cmds.system import System

class Passwords:
    """Class to create and management secrets"""

    pattern = r'[a-z0-9]+\s=\s.+'

    def __init__(self, interactive=None):
        self.check = Checks()
        self.config = Config()
        self.system = System()
        self.config.check_config()
        self.__load()
        self.interactive = interactive
        if interactive == "create": self.create()
        if interactive == "update": self.update()
        if interactive == "remove": self.remove()
    
    def __checks(self, target):
        """Check targets"""
        self.check.check_if_not_exist(self.config.targets_dir + "/" + target + ".yaml", "not found")
    
    def __check_pattern(self, secrets):
        if secret := findall(self.pattern, secrets):
            value = secret[0].split(" = ")
            return value[0], value[1]
        print(f"pattern '{self.pattern}' not match to '{secrets}'")
        sys.exit()
            
    def __load(self):
        """Load secret"""
        file = open(self.config.config_folder + "/passwords.env", "a+", encoding="utf-8")
        file.seek(0)
        try: 
            self.secrets = file.readlines()
        except FileNotFoundError as errors:
            print(errors)
        finally:
            file.close()

    
    def __delete(self, target):
        """Delete secret""" 
        for index, value in enumerate(self.secrets):
            data = sub("=.+\n", "", value)
            if target == data:
                self.secrets.pop(index)
                print(style(f"\nDelete target: {target}", fg="green"))
                self.__save(self.secrets)
                sys.exit()
        print(style(f"\nsecret: {target} not found", fg="yellow"))
    
    def __save(self, secret):
        """Save secret"""
        try: 
            with open(self.config.config_folder + "/secrets.env", 'w', encoding="utf-8") as file:
                file.writelines(secret)
        except FileNotFoundError as errors:
            print(errors)

    def show(self):
        """Show secret"""
        print()
        print(style("Secrets", fg="blue"))
        print(style("#######", fg="blue"))
        print("--------")
        for secret in self.secrets:
            print(style(secret.replace("\n", ""), fg="green"))
            print("--------")

    def create(self, target=None):
        """create secret"""
        if self.interactive == "create":
            Show('targets').show_entity()
            target = prompt("Enter: target = secret")
        target, secret = self.__check_pattern(target)
        self.__checks(target)
        self.__add(target, secret)
        print(style(f"\nAdd secret: {secret} in target: {target}", fg="green"))
    
    def update(self, target=None):
        """Update passwords"""
        if self.interactive == "update":
            self.show()
            target = prompt("Enter: target = secret")
        target, secret = self.__check_pattern(target)
        self.__checks(target)
        self.__add(target, secret, "update")
        print(style(f"\nUpdate secret: {secret} in target: {target}", fg="green"))

    def __add(self, target, secret, action="add"):
        """Add secret"""
        for index, value in enumerate(self.secrets):
            data = sub("=.+\n", "", value)
            if target == data and "add" in action:
                print(style(f"\nInfo: target {target} exist\n", fg="yellow"))
                sys.exit()
            elif target == data and "update" in action: 
                self.secrets[index] = target+"="+secret+"\n"
        if "add" in action: 
            self.secrets.append(target+"="+secret+"\n")
        self.__save(self.secrets)

    def remove(self, target=None):
        """Delete passwords"""
        if self.interactive == "remove":
            self.show()
            target = prompt("Select target to delete")
        self.__delete(target)
