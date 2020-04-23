from qset_core.logging import setup_logging
from qset_core.configuration import ConfigManager, Environment, \
    ENVIRONMENT_NAME_PRODUCTION, \
    ENVIRONMENT_NAME_DEFAULT, \
    ENVIRONMENT_VAR_NAME

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
