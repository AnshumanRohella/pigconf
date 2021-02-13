import yaml


def _parse_config(file, config_key=None):
    config = yaml.safe_load(open(file))

    if config is None:
        raise FileNotFoundError("Could not load the config {}".format(file))

    if config_key is not None:
        config = config.get(config_key)
        if config is None:
            raise KeyError("Could not find the key {} in config {}".format(config_key, file))
    return config

'''

'''
def load_config(file, config_key=None, create=False):
    parsed_config = _parse_config(file, config_key)

    def decorator(cls):
        cls._config = parsed_config
        return cls

    return decorator


def set_attr(attr_name, config_key, attr_type):
    def decorator(cls):
        value = _get_value_from_parsed_config(cls._config, config_key)
        _check_type(value, attr_type)
        setattr(cls, attr_name, value)
        return cls

    return decorator


def _get_value_from_parsed_config(parsed_config, key):
    keys = key.split(".")
    value = parsed_config

    for key in keys:
        value = value.get(key)
        if value is None:
            print("Could not find key: {} in config file.".format(key))
            raise KeyError("Could not find key: {}".format(key))

    return value


def _check_type(val, _type):
    try:
        val = _type(val)
    except ValueError as err:
        print("Could not convert {} to type {}.".format(val, _type))
        raise err
