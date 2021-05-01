"""This module is the main entrypoint of the application."""
import typer

from mulefactory.domain import path_of_exile
from mulefactory.domain import schemas

app = typer.Typer()


@app.command()
def run_path_of_exile(
    username: str,
    password: str,
    game_id: int = 14,
    server: schemas.Server = schemas.Server.standard_sc,
):
    """Run mulefactory CLI for Path of Exile.

    Args:
        username: spply.mulefactory.com username
        password: spply.mulefactory.com password
        game_id: https://supply.mulefactory.com/supply/?gameid=14
        server: Poe League, defaults to standard SC. See above link for options
    """
    server_id: int = server.get_id()
    typer.echo("Started Mulefactory POE scanner for '{server}' ({id})!".format(server=server, id=server_id))
    mule = path_of_exile.POEMulefactory(server_id=server_id)
    mule.login(username=username, password=password)
    response = mule.game_data()
    typer.echo(response.text)
    typer.echo(response.raw)


if __name__ == "__main__":
    app()
