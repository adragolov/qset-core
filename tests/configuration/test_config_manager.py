from qset_core.configuration.config_manager import ConfigManager
from qset_core.configuration.environment import Environment
import pytest


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

    priority_paths = instance.get_priority_paths("logging")

    assert priority_paths is not None
    assert len(priority_paths) == 2
