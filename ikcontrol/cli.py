import click

from init import InitApp
from add_resources import AddResources

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
    initapp.create_config_files()


@click.command(name="add")
@click.option('-k', '--kit', help='kit name that we are installing')
@click.option('-t', '--target', help='destination name where we are going to install the kit')
@click.option('-p', '--pipeline', default=None, help='params to adding at command')
def add(kit, target, pipeline):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    add = AddResources()
    click.echo(kit)

ikctl.add_command(init)
ikctl.add_command(add)
