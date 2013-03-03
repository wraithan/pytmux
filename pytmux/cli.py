"""pytmux - A simple wrapper around tmux.

Usage:
  pytmux list
  pytmux run <config>
  pytmux edit <config> [--copy <other_config>]
  pytmux -h | --help
  pytmux --version

Commands:
  list            Lists all configs.
  run <config>    Runs the specified config.
  edit <config>   Edits the specified config, with --copy will make a new
                  config based on the one specified.

Options:
  -h --help       Show this screen.
  --version       Show version.

"""
from docopt import docopt

from __init__ import __version__
from core import edit_config, list_configs, run_config

def main():
    arguments = docopt(__doc__, version='pytmux {}'.format(__version__))

    if arguments['list']:
        list_configs()
    elif arguments['run']:
        run_config(arguments['config'])
    elif arguments['edit']:
        edit_config(arguments['config'], arguments['copy'],
                    arguments['other_config'])
