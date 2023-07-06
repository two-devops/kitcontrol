import click

from cmds.init import Init
from cmds.add import Add
from cmds.run import Run
from cmds.show import Show
from cmds.secrets import Secrets
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
@click.option('-s', '--sudo', is_flag=True, default=False, show_default=True, help='super user permisions')
@click.option('-i', '--interactive', is_flag=True, default=False, show_default=True, help='Interactive mode to running kits')
def run(kit, target, pipeline, sudo, interactive):
    '''
    command to execute kits
    '''
    if not kit and not target and not pipeline and not sudo and not interactive:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()
 
    action = Run(kit, target, pipeline, sudo)

    if not interactive:
        action.run()
    else:
        action.run_interactive()

@click.command(name="add")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def add(entity_name, name):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    Add(entity_name, name)

@click.command(name="rm")
@click.argument('entity_name', type=click.Choice(ADD))
@click.argument('name')
def rm(entity_name, name):
    '''
    command to remove entities: kits, targets or pipelines
    '''
    Remove(entity_name, name).remove()
    
@click.command(name="show")
@click.argument("entity", type=click.Choice(SHOW))
def show(entity):
    '''
    command to show entities and edit
    '''
    Show(entity).show_entity()

@click.command(name="secrets")
@click.option("-c","--create", help="Add new secret to target")
@click.option("-l","--list", help="List secrets")
@click.option("-u","--update", help="Update secret")
@click.option("-r","--remove", help="Remove secret")
def secrets(create, list, update, remove):
    '''
    command to management secrets
    '''
    Secrets()

kitcontrol.add_command(init)
kitcontrol.add_command(add)
kitcontrol.add_command(run)
kitcontrol.add_command(show)
kitcontrol.add_command(rm)
kitcontrol.add_command(secrets)
