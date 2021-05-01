"""This module is the main entrypoint of the application."""
import typer
from mulefactory.domain import schemas, path_of_exile

app = typer.Typer()


@app.command()
def path_of_exile(username: str, password: str, game_id: int = 14, server: schemas.Server = schemas.Server.standard_sc):
    """

    Args:
        game_id: https://supply.mulefactory.com/supply/?gameid=14
        server_id: Poe League, defaults to standard SC. See above link for options
    """
    server_id: int = server.get_id()
    typer.echo("Started Mulefactory POE scanner for '{server}' ({id})!".format(server=server, id=server_id))
    m = path_of_exile.POEMulefactory()
    m.login(username=username, password=password)
    response = m.get_data()
    typer.echo(response.json())
    


if __name__ == "__main__":
    app()
