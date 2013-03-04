import json
import os
import shutil
import subprocess

import envoy

config_dir = os.path.expanduser('~/.pytmux/')


def get_config_path(filename):
    return os.path.join(config_dir, '{}.json'.format(filename))


def tmux(*args, **kwargs):
    return subprocess.call(('tmux',)+args, **kwargs)


def list_configs():
    configs = [os.path.splitext(fn)[0] for fn in os.listdir(config_dir)
               if os.path.splitext(fn)[1] == '.json']
    print 'Configs:'
    print '\n'.join(configs)


def run_config(config):
    try:
        settings = json.load(open(get_config_path(config)))
    except IOError, e:
        print '{}: "{}"'.format(e.strerror, e.filename)
        return
    except ValueError, e:
        print 'JSON in "{}" is not valid'.format(get_config_path(config))
        return
    retcode = tmux('has-session', '-t', settings['name'],
                   stderr=subprocess.PIPE)

    env = os.environ.get('TMUX')

    base_index = envoy.run('tmux show-options -g base-index').std_out or 0
    if base_index:
        base_index = int(base_index.strip()[-1])

    if retcode:
        # Work around bug in tmux where it wont let you start another session
        # from inside of a session.
        if env:
            del os.environ['TMUX']
        tmux('new-session', '-s', settings['name'], '-d')
        if env:
            os.environ['TMUX'] = env

        # Create windows
        for index, window in enumerate(settings['windows'], base_index):
            name = ()
            if 'name' in window:
                name = ('-n', window['name'])

            tmux('new-window', '-d', '-k', '-t'
                 '{}:{}'.format(settings['name'], index),
                 *name)

            if 'command' in window:
                tmux('send-keys',
                     '-t', '{}:{}'.format(settings['name'], index),
                     window['command'], '^M')

    if env:
        tmux('switch', '-t', settings['name'])
    else:
        tmux('attach-session', '-t', settings['name'])


def edit_config(config, copy, other_config):
    editor = os.environ.get('EDITOR', 'vi')
    filename = get_config_path(config)
    if copy and other_config:
        file_to_copy = get_config_path(other_config)
        shutil.copyfile(file_to_copy, filename)
    subprocess.call('{0} {1}'.format(editor, filename), shell=True)
