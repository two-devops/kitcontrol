import click
from load_config import LoadConfig

class InstallKits:
    """
    Class to install kits on targets

    Attributes:
        options: dict
    Methods:
        kits
        targets
        parameters
    """

    options = {}

    def __init__(self, kits, targets, params) -> None:
        self.options["kits"] = kits
        self.options["targets"] = targets
        self.options["params"] = params


    def install_kits(self):
        print(self.options)
        # click.echo(f"installing {kit} in {target}")

    # def targets(kit, target): 
    #     click.echo(click.style(f"uninstalling {kit} in {target}", fg="red"))

    # def parameters(verbose):
    #     click.echo(f"Verbosity: {verbose}")