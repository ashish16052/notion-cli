import click


@click.group()
def cli():
    pass


@cli.command()
def connect():
    click.echo("Connecting to Notion")


if __name__ == "__main__":
    cli()
