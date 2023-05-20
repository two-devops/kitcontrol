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
    add = Add(entity_name, name)
    add.add_entity()

@click.command(name="show")
@click.argument("entity", type=click.Choice(SHOW))
def show(entity):
    '''
    command to show entities
    '''
    show = Show(entity)
    show.show_entity()

kitcontrol.add_command(init)
kitcontrol.add_command(add)
kitcontrol.add_command(run)
kitcontrol.add_command(show)
