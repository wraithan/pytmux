import os
import subprocess
from collections import OrderedDict


config_dir = os.path.expanduser('~/.pytmux/')


base_config = OrderedDict([
    ('name', 'example'),
    ('windows', [
        OrderedDict([
            ('name', 'editor'),
            ('command', 'emacs'),
        ]), {
            'name': 'default shell',
        }, {
            'command': 'redis-cli MONITOR',
        }, {}
    ])
])


def tmux(*args, **kwargs):
    return subprocess.call(('tmux',)+args, **kwargs)


def get_config_path(filename):
    return os.path.join(config_dir, '{}.json'.format(filename))
