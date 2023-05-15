import click

from cmds.init import Init
from cmds.add import Add
from cmds.run import Run

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
@click.option('-k', '--kit', required=True, help='Kit name')
@click.option('-t', '--target', required=True, help='Target name')
@click.option('-p', '--pipeline', help='Pipeline name')
def run(kit, target, pipeline):
    '''
    command to execute kits
    '''
    execute = Run(kit, target, pipeline)
    execute.run()

@click.command(name="init")
@click.argument("path")
def init(path):
    '''
    command to initialited kitcontrol application
    '''
    init = Init(path)
    init.init_app()

@click.command(name="add")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def add(entity_name, name):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    add = Add()
    add.add_entity(entity_name, name)

kitcontrol.add_command(init)
kitcontrol.add_command(add)
kitcontrol.add_command(run)
