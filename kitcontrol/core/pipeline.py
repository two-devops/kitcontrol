import yaml

from .kit import Kit
from .target import Target

from io import StringIO

BASEPATH = 'pipelines'

class Pipeline:
    def __init__(self, name='commandline', kit='', target='', values={}):
        
        # Use command params...
        if name == 'commandline':
            self.target = Target(target)
            self.kit = Kit(kit, values, osinfo=self.target.osinfo)
        
    def run(self):

        # Upload kit contents and execute on target
        self.target.upload(StringIO(self.kit.contents()), self.kit.config['template'])
        
        return self.target.execute(f"bash {self.kit.config['template']}")
