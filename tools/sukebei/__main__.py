import os.path
import re
from functools import partial

import click

from .enum import get_f_list, get_c_list, WEBSITE_ROOT
from ..utils import GLOBAL_CONTEXT_SETTINGS
from ..utils import print_version as _origin_print_version

print_version = partial(_origin_print_version, 'tools.sukebei')


@click.group(context_settings={**GLOBAL_CONTEXT_SETTINGS}, help=f'Command-Line Tools for {WEBSITE_ROOT}')
@click.option('-v', '--version', is_flag=True,
              callback=print_version, expose_value=False, is_eager=True)
def cli():
    pass  # pragma: no cover


@cli.command('sync', context_settings={**GLOBAL_CONTEXT_SETTINGS},
             help=f'Sync enums for {WEBSITE_ROOT}')
@click.option('-o', '--output_file', 'output_file', type=str,
              default=os.path.join('pynyaasi', 'sukebei', 'enum.py'),
              help='Path to export nyaa.si enum file.', show_default=True)
def sync(output_file):
    with open(output_file, 'w') as f:
        print(f'from enum import Enum, unique', file=f)
        print(f'', file=f)
        print(f'SUKEBEI_ENDPOINT = {WEBSITE_ROOT!r}', file=f)
        print(f'', file=f)
        print(f'', file=f)
        print(f'@unique', file=f)
        print(f'class FilterType(str, Enum):', file=f)
        for f_name, f_value in get_f_list():
            f_e_name = re.sub(r'[\W_]+', '_', f_name).strip('_').upper()
            print(f'    {f_e_name} = {f_value!r}', file=f)

        print(f'', file=f)
        print(f'', file=f)
        print(f'@unique', file=f)
        print(f'class CategoryType(str, Enum):', file=f)
        for c_name, c_value in get_c_list():
            c_e_name = re.sub(r'[\W_]+', '_', c_name).strip('_').upper()
            print(f'    {c_e_name} = {c_value!r}', file=f)


if __name__ == '__main__':
    cli()
