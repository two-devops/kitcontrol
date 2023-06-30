import yaml

from .kit import Kit
from .target import Target

from io import StringIO
from mergedeep import merge
from config.config import Config

BASEPATH = Config.pipelines_dir

class Pipeline:
    def __init__(self, name='commandline', kit='', target='', sudo=False, values: object = {}):
        
        # Use command params...
        if name == 'commandline':
            self.target = Target(target)
            # self.kit = Kit(kit, values)
            targetValues = self.target.config.get('values', {})
            self.kit = Kit(kit, merge(targetValues, values))
            self.sudo = sudo
        
        else:
            self.name = name
            self.config = self._load_config()
            self.sudo = self.config.get('sudo', False)

    def _load_config(self):
        return yaml.load(open(f"{BASEPATH}/{self.name}.yaml", "r"), Loader=yaml.loader.SafeLoader)


    def start(self):

        # Run every kit on every target...
        for target in self.config['targets']:
            self.target = Target(target)
            
            for kit in self.config['kits']:

                # Values treatment
                targetValues = self.target.config.get('values', {})
                pipelineValues = self.config['values'].get(target, {}).get(kit, {})
                
                self.kit = Kit(kit, merge(targetValues, pipelineValues))

                self.run()


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
        self.target.execute(f"bash pipeline.sh", sudo=self.sudo)