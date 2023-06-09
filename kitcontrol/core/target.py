import yaml

from .osinfo import OsInfo
from .connection import FabricConnection
from config.config import Config

BASEPATH = Config.targets_dir

class Target:
    def __init__(self, name, connection=FabricConnection()):

        self.name = name
        self.connection = connection

        # Load target config
        self.config = self._load_config()

        # Try to connect and auto-detect
        self.connection.connect(
            self.config.get('host'), 
            self.config.get('user', None), 
            self.config.get('port', None),
            self.config.get('args', None),
            self.config.get('sudo', None),
        )

        # Autodetect: osinfo + hostname + connectivity (online/offline) ?
        self.osinfo = self.autodetect()

    def _load_config(self):
        return yaml.load(open(f"{BASEPATH}/{self.name}.yaml", "r"), Loader=yaml.loader.SafeLoader)

    def execute(self, command, hide=False, sudo=False):
        return self.connection.execute(command, hide, sudo)
    
    def upload(self, file, target=None):
        return self.connection.upload(file, target)
    
    def download(self, file, target=None):
        return self.connection.download(file, target)

    def autodetect(self):
        osinfo = {}

        if release := self.execute("cat /etc/os-release", hide=True):
            for line in release.stdout.splitlines():
                key, value = line.split("=")
                osinfo[key] = value.strip('"')
        
        return OsInfo(
            osinfo.get("ID"), 
            osinfo.get("VERSION_ID"), 
            osinfo.get("NAME"), 
            osinfo.get("PRETTY_NAME"), 
            osinfo.get("VERSION_CODENAME"),
        )
