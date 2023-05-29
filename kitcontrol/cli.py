import click

from cmds.init import Init
from cmds.add import Add
from cmds.run import Run
from cmds.show import Show

ADD = ["kit", "target", "pipeline"]
SHOW = ["kits", "targets", "pipelines"]

@click.group(name='kitcontrol')
def kitcontrol():
    '''
    Tool for automatic process
    '''
    pass

@click.command(name="init")
@click.argument("path")
def init(path):
    '''
    command to initialited kitcontrol application
    '''
    init = Init(path)
    init.init_app()

@click.command(name="run")
@click.option('-k', '--kit', required=True, help='Kit name')
@click.option('-t', '--target', required=True, help='Target name')
@click.option('-p', '--pipeline', help='Pipeline name')
@click.option('-s', '--sudo', help='super user permisions')
def run(kit, target, pipeline, sudo):
    '''
    command to execute kits
    '''
    execute = Run(kit, target, pipeline, sudo)
    execute.run()

@click.command(name="add")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def add(entity_name, name):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    Add(entity_name, name)

@click.command(name="show")
@click.option("-e", "--edit",help="edit kits, target or pipelines")
@click.argument("entity", type=click.Choice(SHOW))
def show(entity, edit):
    '''
    command to show entities and edit
    '''
    Show(entity, edit)

kitcontrol.add_command(init)
kitcontrol.add_command(add)
kitcontrol.add_command(run)
kitcontrol.add_command(show)
