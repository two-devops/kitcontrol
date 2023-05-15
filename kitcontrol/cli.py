import click

from cmds.init import InitApp
from cmds.system import System
from cmds.config import Config
from cmds.add import AddResources
from core.pipeline import Pipeline

ADD = [
    "kit",
    "target",
    "pipeline"
]

@click.group(name='kitcontrol')
def kitcontrol():
    '''
    Tool for automatic process
    '''
    pass

@click.command(name="run")
@click.option('-k', '--kit', default=None, help='Kit name')
@click.option('-t', '--target', default=None, help='Target name')
@click.option('-p', '--pipeline', default=None, help='Pipeline name')
def run(kit, target, pipeline):
    '''
    command to execute kits
    '''
    system = System()
    config = Config()
    if  system.search(config.CONFIG_FILE):
        pipeline = Pipeline(kit=kit, target=target)
        pipeline.run()
    else:
        click.echo(".kitcontrol folder not found")

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
kitcontrol.add_command(run)
