import click

from cmds.init import Init
from cmds.add import Add
from cmds.run import Run
from cmds.show import Show
from cmds.wizard import Wizard
from cmds.remove import Remove

ADD = ["kit", "target", "pipeline"]
SHOW = ["kits", "targets", "pipelines"]

@click.group(name='kitcontrol')
def kitcontrol():
    '''
    Tool for automatic process
    '''
    pass

@click.command(name="init")
@click.argument("path", nargs=-1)
def init(path):
    '''
    command to initialited kitcontrol application
    '''
    action = Init(path)
    action.init_app()

@click.command(name="run")
@click.option('-k', '--kit', help='Kit name')
@click.option('-t', '--target', help='Target name')
@click.option('-p', '--pipeline', help='Pipeline name')
@click.option('-s', '--sudo', help='super user permisions')
def run(kit, target, pipeline, sudo):
    '''
    command to execute kits
    '''
    action = Run(kit, target, pipeline, sudo)
    action.run()

@click.command(name="add")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def add(entity_name, name):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    acition = Add(entity_name, name)
    acition.create()

@click.command(name="rm")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def rm(entity_name, name):
    '''
    command to remove entities: kits, targets or pipelines
    '''
    action = Remove(entity_name, name)
    action.remove()
    

@click.command(name="show")
@click.option("-e", "--edit",help="edit kits, target or pipelines")
@click.argument("entity", type=click.Choice(SHOW))
def show(entity, edit):
    '''
    command to show entities and edit
    '''
    Show(entity, edit)

@click.command(name="wizard")
@click.argument("entity", type=click.Choice(ADD))
def wizard(entity):
    '''
    command to show entities and edit
    '''
    Wizard(entity)

kitcontrol.add_command(init)
kitcontrol.add_command(add)
kitcontrol.add_command(run)
kitcontrol.add_command(show)
kitcontrol.add_command(rm)
kitcontrol.add_command(wizard)
