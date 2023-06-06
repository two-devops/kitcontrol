from abc import ABCMeta, abstractmethod
from fabric import Connection as fabConnection, Config as fabConfig

class Connection(metaclass=ABCMeta):
    """Interface for provider connections"""
    
    @abstractmethod
    def connect(self, host, user=None, port=None, args=None, sudo=None):
        """Connect to target"""
    
    @abstractmethod
    def execute(self, command, hide=False, sudo=False):
        """Execute command"""
    
    @abstractmethod
    def upload(self, file):
        """Upload a file"""
    
    @abstractmethod
    def download(self, file):
        """Download a file"""


class FabricConnection(Connection):

    def connect(self, host, user=None, port=None, args=None, sudo=None):
        if sudo:
            config = fabConfig({'sudo': sudo})
        else:
            config = fabConfig({'sudo': {'password': args.get('password', None)}})

        self.connection = fabConnection(host, user, port, config, connect_kwargs=args)

    def execute(self, command, hide=False, sudo=False):
        if sudo:
            return self.connection.sudo(command, hide=hide)
        
        return self.connection.run(command, hide=hide)
    
    def upload(self, file, target=None):
        return self.connection.put(file, target)

    def download(self, file, target=None):
        return self.connection.get(file, target)


class FakeConnection(Connection):
    def connect(self, host, user=None, port=None, args=None, sudo=None):
        self.connection = {"host": host, "user": user, "port": port, "args": args, "sudo": sudo}

    def execute(self, command, hide=False, sudo=False):
        return f"Executed command {command}"
    
    def upload(self, file, target=None):
        return f"Uploaded file {file}"

    def download(self, file, target=None):
        return f"Downloaded file {file}"