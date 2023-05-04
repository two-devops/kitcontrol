from abc import ABCMeta, abstractmethod

class Connection(metaclass=ABCMeta):
    
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
    pass

class FakeConnection(Connection):
    pass