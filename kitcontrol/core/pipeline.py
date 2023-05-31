import yaml

from .kit import Kit
from .target import Target

from io import StringIO

BASEPATH = 'pipelines'

class Pipeline:
    def __init__(self, name='commandline', kit='', target='', values: object = {}):
        # Use command params...
        if name == 'commandline':
            self.target = Target(target)
            self.kit = Kit(kit, values)
        
    def run(self):

        pipeline = ""

        # Get all files from kit
        files = self.kit.getFiles(self.target.osinfo)

        # Upload each file, and add to pipeline.sh if it's executable...
        for name, file in files.items():

            self.target.upload(file, name)

            if name.endswith(".sh"):
                pipeline += f"bash {name}\n"
            
            elif name.endswith(".py"):
                pipeline += f"python {name}\n"

        # Finally upload and execute "bash pipeline.sh" with sudo if indicated on params / config
        self.target.upload(StringIO(pipeline), "pipeline.sh")
        self.target.execute(f"bash pipeline.sh", sudo=True)