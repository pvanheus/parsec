import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('upload_file_from_url')
@click.argument("library_id", type=str)
@click.argument("file_url", type=str)

@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded file. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--file_type",
    help="Galaxy file format name",
    default="auto",
    show_default=True,
    type=str
)
@click.option(
    "--dbkey",
    help="Dbkey",
    default="?",
    show_default=True,
    type=str
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id, file_url, folder_id="", file_type="auto", dbkey="?"):
    """Upload a file to a library from a URL.

Output:

    
    """
    return ctx.gi.libraries.upload_file_from_url(library_id, file_url, folder_id=folder_id, file_type=file_type, dbkey=dbkey)
