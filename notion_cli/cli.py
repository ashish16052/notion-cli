import click
from notion_cli.auth import write_token


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--secret",
    prompt="Enter your notion integration secret",
    help="Your notion integration secret.",
)
def connect(secret):
    write_token(secret)
    click.echo("Added notion integration secret succesfuly")
