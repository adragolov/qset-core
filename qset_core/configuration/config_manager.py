from .environment import Environment
from threading import RLock
from logging import getLogger, Logger
from qset_core.logging import setup_logging
import os


class ConfigManager:

    __Default = None
    __Lock = RLock()

    def __init__(self, environment: Environment = None):
        self._env: Environment = environment or Environment.get_default()
        self._logger: Logger = self.create_logger("ConfigManager")

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
        candidate_file_paths = [
            f"{root}/{configuration_name}.{extension}",
            f"{root}/{configuration_name}.{self.environment.environment_name}.{extension}"
        ]
        result = []
        for candidate_path in candidate_file_paths:
            if os.path.exists(candidate_path):
                result.append(candidate_path)
        return result

    def _configure_loggers(self):
        logging_config_paths = self.get_priority_paths("config.logging")
        setup_logging(logging_config_paths)

    def create_logger(self, logger_name: str = 'global') -> Logger:
        self._configure_loggers()
        return getLogger(logger_name)
