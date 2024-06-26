import os
import json
import click
from .calculate_sha1 import calculate_all_sha1_in_folder
from .compare_dicts import compare_dicts

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    pass

@cli.command()
@click.option('--directory', '-d', default=os.getcwd(), help='target directory path')
@click.option('--output', '-o', default=f'{os.getcwd()}/sha1.json', help='output sha1 json path')
def calculate(directory, output):
    sha1_dict = calculate_all_sha1_in_folder(directory)

    with open(output, 'w') as file:
        json.dump(sha1_dict, file, indent=2)

@cli.command()
@click.argument('sha1_json_path', type=click.Path(exists=True), nargs=2)
@click.option('--output', '-o', default=f'{os.getcwd()}/validation_result.json', help='validation result json path')
@click.option('--pattern', '-p', default=['*'], help='fnmatch pattern for file path', multiple=True)
@click.option('--validate-by-file', '-f', is_flag=True, help='validate by file, if not set, validate by filepath')
def validate(sha1_json_path, output, pattern, validate_by_file):
    with open(sha1_json_path[0], 'r') as file:
        first_sha1_dict = json.load(file)

    with open(sha1_json_path[1], 'r') as file:
        second_sha1_dict = json.load(file)

    different, first_only, second_only = compare_dicts(first_sha1_dict, second_sha1_dict, pattern, validate_by_file)
    json_dict = {
        'different': different,
        'only_in_first': first_only,
        'only_in_second': second_only
    }

    with open(output, 'w') as file:
        json.dump(json_dict, file, indent=2)


if __name__ == "__main__":
    cli()