import os
import shutil
import subprocess


config_dir = os.path.expanduser('~/.pytmux/')


def list_configs():
    configs = [os.path.splitext(fn)[0] for fn in os.listdir(config_dir)
               if os.path.splitext(fn)[1] == '.json']
    print 'Configs:'
    print '\n'.join(configs)


def run_config(config):
    raise NotImplementedError


def edit_config(config, copy, other_config):
    editor = os.environ.get('EDITOR', 'vi')
    filename = os.path.join(config_dir, '{}.json'.format(config))
    if copy and other_config:
        file_to_copy = os.path.join(config_dir, '{}.json'.format(other_config))
        shutil.copyfile(file_to_copy, filename)
    subprocess.call('{0} {1}'.format(editor, filename), shell=True)
