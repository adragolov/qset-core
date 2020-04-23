import logging
import logging.config
import hiyapyco
import os


def setup_logging(
        config_file_paths: [str] = None,
        default_level=logging.NOTSET):

    if config_file_paths is not None:
        for file_path in config_file_paths:
            if not os.path.exists(file_path):
                raise IOError(f"Logging file '{file_path}' could not be found.")

    if config_file_paths is not None and len(config_file_paths) > 0:
        logging_config = hiyapyco.load(*config_file_paths)
        logging.config.dictConfig(logging_config)
    else:
        logging.basicConfig(level=default_level)
