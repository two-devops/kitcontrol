import click

from init import InitApp


@click.group(name='ikctl')
def ikctl():
    '''
    App to install Kits on targets
    '''
    pass


@click.command(name="install")
@click.option('-k', '--kit', required=True, help='kit name that we are installing')
@click.option('-t', '--target', required=True, help='destination name where we are going to install the kit')
@click.option('-pa', '--params', required=False, default=None, help='params to adding at command')
def install(kit, target, params):

    """
    command to run kits on select target/s
    """

    click.echo(kit, target, params)


@click.command(name="init")
@click.argument("path")
def init(path):
    '''
    command to initialited ikctl application
    '''
    initapp = InitApp(path)
    initapp.build()


@click.command(name="add")
@click.argument('name_option')
def add(name_option):
    '''
    command to adding entities: kits, targets or pipelines
    '''
    click.echo(name_option)


@click.command(name="pipeline")
@click.argument('name_pipeline')
def pipeline(name_pipelile):
    '''
    command to run pipeline
    '''
    click.echo(name_pipelile)


ikctl.add_command(init)
ikctl.add_command(add)
ikctl.add_command(pipeline)
ikctl.add_command(install)
