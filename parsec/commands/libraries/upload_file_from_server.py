import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('upload_file_from_server')
@click.argument("library_id", type=str)
@click.argument("server_dir", type=str)

@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded files. If not provided, the root folder will be used",
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
@click.option(
    "--link_data_only",
    help="either 'copy_files' (default) or 'link_to_files'. Setting to 'link_to_files' symlinks instead of copying the files",
    type=str
)
@click.option(
    "--roles",
    help="???",
    type=str
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id, server_dir, folder_id="", file_type="auto", dbkey="?", link_data_only="", roles=""):
    """Upload all files in the specified subdirectory of the Galaxy library import directory to a library.

Output:

    
    """
    return ctx.gi.libraries.upload_file_from_server(library_id, server_dir, folder_id=folder_id, file_type=file_type, dbkey=dbkey, link_data_only=link_data_only, roles=roles)
