import yaml

from jinja2 import Environment, FileSystemLoader
from mergedeep import merge
from os.path import exists
from io import StringIO

BASEPATH = 'kits'

class Kit:
    def __init__(self, name, values={}):

        self.name = name

        # Load kit config
        self.config = self._load_config()

        # Merge values
        self.data = merge(self.config['data'], values)

        # Set jinja2 environment (templates dir)
        self.env = Environment(loader=FileSystemLoader(f"{BASEPATH}/{self.name}/"))

    def _load_config(self):
        return yaml.load(open(f"{BASEPATH}/{self.name}/{self.name}.yaml", "r"), Loader=yaml.loader.SafeLoader)


    def getFiles(self, osInfo=None):

        files = {}

        for filename in self.config['files']:

            # Distro prefix
            if osInfo and exists(f"{BASEPATH}/{self.name}/{osInfo.id}-{filename}"):
                filename = f"{osInfo.id}-{filename}"

            # Load template
            template = self.env.get_template(filename)
            
            # Add to dict files
            data = merge(self.data, {"osInfo": osInfo}) if osInfo else self.data
            files[filename] = StringIO(template.render(data))

        return files