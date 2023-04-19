import yaml
from fabric import Connection

class Target:
    def __init__(self, name):

        # Load target config
        config = yaml.load(open(f"targets/{name}.yaml", "r"), Loader=yaml.loader.SafeLoader)

        self.name = config['name']
        self.host = config['host']
        self.user = config['user']
        self.args = config['args']

        # Try to connect and auto-detect
        self.connection = self.get_connection()

    def get_connection(self):
        return Connection(self.host, self.user, connect_kwargs=self.args)

    def execute(self, command):
        return self.connection.run(command)
    
    def upload(self):
        pass