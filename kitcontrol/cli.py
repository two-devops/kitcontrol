import click

from init import InitApp
from add import AddResources

ADD = [
    "kit",
    "target",
    "pipeline"
]

@click.group(name='kitcontrol')
@click.option('-k', '--kit', default=None, help='kit name')
@click.option('-t', '--target', default=None, help='Destination on running the kit')
@click.option('-p', '--pipeline', default=None, help='Choose pipeline name')
def kitcontrol(kit, target, pipeline):
    '''
    App to install Kits on targets
    '''
    pass

@click.command(name="init")
@click.argument("path")
def init(path):
    '''
    command to initialited kitcontrol application
    '''
    initapp = InitApp(path)
    initapp.init_app()

@click.command(name="add")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def add(entity_name, name):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    added = AddResources()
    added.add_entity(entity_name, name)

kitcontrol.add_command(init)
kitcontrol.add_command(add)
