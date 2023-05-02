import click

from init import InitApp
from add import AddResources

ADD = [
    "kit",
    "target",
    "pipeline"
]

CONFIG_NAME = "kitcontrol.yaml"

@click.group(name='ikctl')
def ikctl():
    '''
    App to install Kits on targets
    '''
    pass

@click.command(name="init")
@click.argument("path")
def init(path):
    '''
    command to initialited ikctl application
    '''
    initapp = InitApp(path)
    initapp.build_folders()
    initapp.create_config_files(CONFIG_NAME)


@click.command(name="add")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def add(entity_name, name):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    added = AddResources()
    added.add_kit(entity_name, name)

ikctl.add_command(init)
ikctl.add_command(add)
