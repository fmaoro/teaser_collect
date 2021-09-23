
import configparser

from pkg_resources import resource_stream


def load_config(config_filename=None):
    """
    Reads the config file and adds any settings in it to the default settings

    :param config_filename:
    :return: A ConfigParser object full of settings
    """
    config = configparser.SafeConfigParser()

    # first, read the defaults
    if config_filename:
        print("loading_config for " + config_filename)
        try:
            with open(config_filename) as f:
                config.read_file(f)
        except Exception as e:
            print(e)

    else:
        config.read_file(resource_stream('twitter_data_collection.etc', config_filename))

    return config
