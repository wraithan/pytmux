import json
import os
import shutil
import subprocess

import envoy

from schema import validate_config
from utils import base_config, config_dir, get_config_path, Tmux


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

    tmux = Tmux(settings['name'], settings.get('directory'))

    make_session = tmux.call('has-session', '-t', settings['name'],
                             stderr=subprocess.PIPE)

    base_index = envoy.run('tmux show-options -g base-index').std_out or 0
    if base_index:
        base_index = int(base_index.strip()[-1])

    if make_session:
        tmux.create()

        # Create windows
        for index, window in enumerate(settings['windows'], base_index):
            tmux.new_window(index, window.get('name'))
            if 'command' in window:
                tmux.send_keys(index, window['command'])

    tmux.attach()



def edit_config(config, copy, other_config):
    editor = os.environ.get('EDITOR', 'vi')
    filename = get_config_path(config)
    if copy and other_config:
        file_to_copy = get_config_path(other_config)
        shutil.copyfile(file_to_copy, filename)
    elif not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(base_config, indent=2))
    subprocess.call('{0} {1}'.format(editor, filename), shell=True)


def doctor_command():
    configs = [os.path.splitext(fn)[0] for fn in os.listdir(config_dir)
               if os.path.splitext(fn)[1] == '.json']
    for conf in configs:
        validate_config(conf)
