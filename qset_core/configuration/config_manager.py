from .environment import Environment
from threading import RLock
import os


class ConfigManager:

    __Default = None
    __Lock = RLock()

    def __init__(self, environment: Environment = None):
        self._env: Environment = environment or Environment.get_default()

    @property
    def environment(self) -> Environment:
        return self._env

    @classmethod
    def get_default(cls):
        if cls.__Default is None:
            with cls.__Lock:
                if cls.__Default is None:
                    cls.__Default = ConfigManager()
        return cls.__Default

    def get_priority_paths(self, configuration_name: str, extension: str = "yaml") -> [str]:
        root = os.getcwd()
        return [
            f"{root}/{configuration_name}.{extension}",
            f"{root}/{configuration_name}.{self.environment.environment_name}.{extension}"
        ]
