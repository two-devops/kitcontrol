import sys
from click import echo, style

from cmds.system import System
from cmds.config import Config

class Checks:
    """class to check folders and files"""

    def __init__(self) -> None:
        self.config = Config()
        self.system = System()

    def check_if_not_exist(self, path, message=None):
        """check if exist folder"""
        if not self.system.search(path):
            echo(style(f"\nInfo: {path} {message}\n", fg="yellow"))
            sys.exit()

    def check_if_exist(self, path, message=None):
        """check if exist folder"""
        if self.system.search(path):
            echo(style(f"\nInfo: {path} {message}\n", fg="yellow"))
            sys.exit()
    