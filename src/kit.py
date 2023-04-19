import yaml

from jinja2 import Environment, FileSystemLoader
from mergedeep import merge

class Kit:
    def __init__(self, name, values={}):

        # Load kit config
        config = yaml.load(open(f"kits/{name}/{name}.yaml", "r"), Loader=yaml.loader.SafeLoader)

        self.name = config['name']
        self.data = config['data']

        # Merge values
        self.data = merge(self.data, values)

        # Load template
        env = Environment(loader=FileSystemLoader(f"kits/{name}/"))
        self.template = env.get_template(config['template'])

    def contents(self):
        return self.template.render(self.data)