import yaml
from fabric import Connection

BASEPATH = 'targets'

class Target:
    def __init__(self, name):

        self.name = name

        # Load target config
        self.config = self._load_config()

        # Try to connect and auto-detect
        self.connection = self.get_connection()
        self.osinfo = self.autodetect()

    def _load_config(self):
        return yaml.load(open(f"{BASEPATH}/{self.name}.yaml", "r"), Loader=yaml.loader.SafeLoader)

    def get_connection(self):
        return Connection(self.config.get('host'), 
                          self.config.get('user', None), 
                          self.config.get('port', None),
                          connect_kwargs=self.config.get('args', None))

    def execute(self, command):
        return self.connection.run(command, hide=True)
    
    def upload(self, file):
        return self.connection.put(file)
    
    def autodetect(self):
        osinfo = {}

        if release := self.execute("cat /etc/os-release"):
            for line in release.stdout.splitlines():
                key, value = line.split("=")
                osinfo[key] = value.strip('"')
        
        return osinfo
