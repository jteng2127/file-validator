import os
import json
import click
from .calculate_sha1 import calculate_all_sha1_in_folder

@click.group()
def cli():
    pass

@cli.command()
@click.option('--directory', '-d', default=os.getcwd(), help='target directory path')
@click.option('--output', '-o', default=f'{os.getcwd()}/sha1.json', help='output sha1 json path')
def cal(directory, output):
    sha1_dict = calculate_all_sha1_in_folder(directory)

    with open(output, 'w') as file:
        json.dump(sha1_dict, file, indent=2)

if __name__ == "__main__":
    cli()