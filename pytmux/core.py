import os


config_dir = os.path.expanduser('~/.pytmux/')


def list_configs():
    configs = [os.path.splitext(fn)[0] for fn in os.listdir(config_dir)
               if os.path.splitext(fn)[1] == '.json']
    print 'Configs:'
    print '\n'.join(configs)


def run_config(config):
    raise NotImplementedError


def edit_config(config, copy, other_config):
    raise NotImplementedError
