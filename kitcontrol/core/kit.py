import yaml

from jinja2 import Environment, FileSystemLoader
from mergedeep import merge

BASEPATH = 'kits'

class Kit:
    def __init__(self, name, values={}, osinfo=None):

        self.name = name

        # Load kit config
        self.config = self._load_config()

        # Merge values
        self.data = merge(self.config['data'], values)

        # Load template 
        self.template = self._load_template(osinfo)

    def _load_config(self):
        return yaml.load(open(f"{BASEPATH}/{self.name}/{self.name}.yaml", "r"), Loader=yaml.loader.SafeLoader)

    def _load_template(self, osinfo=None):
        env = Environment(loader=FileSystemLoader(f"{BASEPATH}/{self.name}/"))
        
        return env.get_template((osinfo.id + '-' if osinfo else '') + self.config['template'])

    def contents(self):
        return self.template.render(self.data)