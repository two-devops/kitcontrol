from click import echo, style

from config.config import Config

from cmds.system import System
from cmds.checks import Checks

class Init:
    """Initiated Application"""

    characters = "."

    def __init__(self, path=None):
        self.path = path if path else "."
        self.system = System()
        self.config = Config()
        self.check = Checks()
        self.folders = [self.config.config_folder, self.config.kits_dir, self.config.targets_dir, self.config.pipelines_dir]

    def init_app(self):
        """Build folders"""

        # This "if" is because cli argument sent to us tuple when we are typing "kitcontrol init <argument>" 
        if isinstance(self.path, tuple):
            self.path = ''.join(self.path)

        # Check if exist folder
        if self.path and self.path not in self.characters:
            self.check.check_if_exist(self.path, "already exist")

        # Create folders and config file
        for folder in self.folders:
            if self.path != self.characters:
                if not self.system.command('mkdir -p ' + self.path + '/' + folder):
                    echo(style("Error: unknown", fg="red"))
                else:
                    echo(style(f"directory {self.path}/{folder} created", fg="green"))

                if folder == self.config.config_folder:
                    path = self.path + "/" + folder
                    self.system.mkfile(path, self.config.config_file_name, self.config.load_default(self.config.config_file_name))
            else:
                if not self.system.command('mkdir -p ' + folder):
                    echo(style("Error: unknown", fg="red"))
                else:
                    echo(style(f"directory {folder} created", fg="green"))

                if folder == self.config.config_folder:
                    self.system.mkfile(self.config.config_folder, self.config.config_file_name, self.config.load_default(self.config.config_file_name))
