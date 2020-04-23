import os
from threading import RLock

ENVIRONMENT_VAR_NAME: str = "QSET_ENVIRONMENT"
ENVIRONMENT_NAME_DEFAULT: str = 'Development'
ENVIRONMENT_NAME_PRODUCTION: str = 'Production'


class Environment:

    __Default = None
    __Lock = RLock()

    def __init__(self, environment_name: str = None):
        self._environment_name: str = (environment_name or os.getenv(ENVIRONMENT_VAR_NAME, ENVIRONMENT_NAME_DEFAULT))\
            .strip()

    @property
    def environment_name(self) -> str:
        return self._environment_name

    @classmethod
    def get_default(cls):
        if cls.__Default is None:
            with cls.__Lock:
                if cls.__Default is None:
                    cls.__Default = Environment()
        return cls.__Default
