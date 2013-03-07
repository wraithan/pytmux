import json
from jsonschema import Draft3Validator
from utils import get_config_path


schema = {
    'type': 'object',
    'required': True,
    'additionalProperties': False,
    'properties': {
        'name': {
            'type': 'string',
            'required': True
        },
        'windows': {
            'type': 'array',
            'required': True,
            'minItems': 1,
            'items': {
                'type': 'object',
                'required': True,
                'additionalProperties': False,
                'properties': {
                    'name': {
                        'type': 'string'
                    },
                    'command': {
                        'type': 'string'
                    }
                }
            }
        }
    }
}


def validate_config(config):
    filename = get_config_path(config)
    try:
        to_validate = json.load(open(filename))
    except ValueError, e:
        print '{}: {}'.format(filename, e)
        return

    validator = Draft3Validator(schema)

    for error in sorted(validator.iter_errors(to_validate), key=str):
        print '{}: {}'.format(filename, error)
