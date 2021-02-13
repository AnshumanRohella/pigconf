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
Loads the configuraion yaml file to be mapped.
Fails with FileNotFoundError if the file doesn't exist.

    Parameters
    ----------
    file : str
        Absolute path to the yaml configuration file.
    config_key : str
        The "base key" to load the configuration from. If not defined, 
        the whole yaml is loaded to be mapped and the configuration class
        has access to all the configuration objects.

    Returns
    -------
    decorator for the config class.
'''
def load_config(file, config_key=None):
    parsed_config = _parse_config(file, config_key)

    def decorator(cls):
        cls._config = parsed_config
        return cls

    return decorator

"""
Sets the attribute for the corresponding configuration class.

    Parameters
    ----------
    attr_name : str
        The name of the attribute to be created for the class as a class attribute
    config_key : str
        A '.' separated string to specify the key in yaml config file whose value shall be 
        used as the attribute
    attr_type : builtin type class
        A built in python type to specify the conversion of the attributes.
    
    Returns
    -------
    decorator for the config class.
"""
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
            raise KeyError(f"Could not find key: {key} in config file.")

    return value


def _check_type(val, _type):
    try:
        val = _type(val)
    except ValueError as err:
        raise ValueError(f"Could not convert {val} to type {_type}.")
