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


def get_config_path(filename):
    return os.path.join(config_dir, '{}.json'.format(filename))


class Tmux(object):
    def __init__(self, session=None, socket=None):
        self.session = session

    def call(self, *args, **kwargs):
        command = ('tmux',)
        print command+args
        return subprocess.call(command+args, **kwargs)

    def create(self):
        # Work around bug in tmux where it wont let you start another session
        # from inside of a session.
        env = os.environ.get('TMUX')
        if env:
            del os.environ['TMUX']

        self.call('new-session', '-s', self.session, '-d')

        if env:
            os.environ['TMUX'] = env

    def send_keys(self, window, command):
        return self.call('send-keys',
                         '-t', '{}:{}.'.format(self.session, window),
                         command, '^M')

    def attach(self):
        if os.environ.get('TMUX'):
            self.call('switch', '-t', self.session)
        else:
            self.call('attach-session', '-t', self.session)

    def new_window(self, number, name):
        name_arg = ()
        if name:
            name_arg = ('-n', name)

        self.call('new-window', '-d', '-k',
                  '-t', '{}:{}'.format(self.session, number),
                  *name_arg)
