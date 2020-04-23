from qset_core.configuration import ConfigManager, Environment
import pytest
import logging
import os


def test_constructor_with_ctor_param():
    env = Environment.get_default()
    instance = ConfigManager(env)
    assert instance is not None
    assert instance.environment is not None
    assert instance.environment.environment_name == env.environment_name
    assert instance.environment is env


def test_constructor_without_ctor_param():
    instance = ConfigManager()
    assert instance is not None
    assert instance.environment is not None


def test_shared_config_manager():
    instance1 = ConfigManager.get_default()
    instance2 = ConfigManager.get_default()

    assert instance1 is not None
    assert instance2 is not None
    assert instance2 is instance1, "Multiple calls to get_default() must result in the same instance."


def test_get_priority_paths():
    instance = ConfigManager.get_default()

    with pytest.raises(TypeError):
        instance.get_priority_paths()

    priority_paths = instance.get_priority_paths("config.logging")

    assert priority_paths is not None
    assert isinstance(priority_paths, list)


def test_get_priority_paths_exist():
    priority_paths = ConfigManager.get_default().get_priority_paths("config.logging")

    assert len(priority_paths) >= 1, "The default logging configuration file MUST be present."

    for path in priority_paths:
        assert isinstance(path, str)
        assert os.path.exists(path)


def test_create_logger():
    instance = ConfigManager.get_default()
    logger = instance.create_logger("unit_test")

    assert logger is not None
    assert isinstance(logger, logging.Logger)
