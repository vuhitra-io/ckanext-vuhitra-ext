import click


@click.group(short_help="vuhitra_ext CLI.")
def vuhitra_ext():
    """vuhitra_ext CLI.
    """
    pass


@vuhitra_ext.command()
@click.argument("name", default="vuhitra_ext")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [vuhitra_ext]
