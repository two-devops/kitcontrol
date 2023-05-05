from abc import ABCMeta, abstractmethod
from fabric import Connection as fabConnection

class Connection(metaclass=ABCMeta):
    """Interface for provider connections"""
    
    @abstractmethod
    def connect(self, host, user=None, port=None, args=None):
        """Connect to target"""
    
    @abstractmethod
    def execute(self, command):
        """Execute command"""
    
    @abstractmethod
    def upload(self, file):
        """Upload a file"""
    
    @abstractmethod
    def download(self, file):
        """Download a file"""


class FabricConnection(Connection):

    def connect(self, host, user=None, port=None, args=None):
        self.connection = fabConnection(host, user, port, connect_kwargs=args)

    def execute(self, command):
        return self.connection.run(command, hide=True)
    
    def upload(self, file, target=None):
        return self.connection.put(file, target)

    def download(self, file, target=None):
        return self.connection.get(file, target)


class FakeConnection(Connection):
    def connect(self, host, user=None, port=None, args=None):
        self.connection = {"host": host, "user": user, "port": port, "args": args}

    def execute(self, command):
        return f"Executed command {command}"
    
    def upload(self, file, target=None):
        return f"Uploaded file {file}"

    def download(self, file, target=None):
        return f"Downloaded file {file}"