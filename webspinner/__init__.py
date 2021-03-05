import configparser

__author__ = "Elaine T. Hale"
__email__ = "elaine.hale@nrel.gov"

from ._version import __version__

class WebspinnerRuntimeError(RuntimeError): pass

WEBSPINNER_CONFIGURATION = None

def configure(config_filename):
    """
    Configure webspinner by loading a config file with optional sections '[AWS]'
    and/or '[PGRES]'

    Parameters
    ----------
    config_filename : pathlib.Path or str
    """
    global WEBSPINNER_CONFIGURATION
    config = configparser.ConfigParser()
    config.read(config_filename)
    WEBSPINNER_CONFIGURATION = config
