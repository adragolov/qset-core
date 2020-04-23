from qset_core.configuration.environment import Environment, \
    ENVIRONMENT_VAR_NAME, \
    ENVIRONMENT_NAME_DEFAULT, \
    ENVIRONMENT_NAME_PRODUCTION
import os


TEST_ENV = "test"


def test_constants():
    assert ENVIRONMENT_VAR_NAME is not None
    assert ENVIRONMENT_VAR_NAME == "QSET_ENVIRONMENT"
    assert ENVIRONMENT_NAME_DEFAULT is not None
    assert ENVIRONMENT_NAME_PRODUCTION is not None
    assert ENVIRONMENT_NAME_DEFAULT != ENVIRONMENT_NAME_PRODUCTION, "Default environment should not be a production one"


def test_constructor_with_ctor_param():
    instance = Environment(TEST_ENV)
    assert instance is not None
    assert instance.environment_name is not None
    assert instance.environment_name == TEST_ENV

    another_instance = Environment(TEST_ENV)
    assert another_instance.environment_name == instance.environment_name


def test_constructor_with_ctor_param_leading_white_space():
    instance = Environment(f"   {TEST_ENV}")
    assert instance is not None
    assert instance.environment_name is not None
    assert instance.environment_name == TEST_ENV

    another_instance = Environment(TEST_ENV)
    assert another_instance.environment_name == instance.environment_name


def test_constructor_with_ctor_param_trailing_white_space():
    instance = Environment(f"{TEST_ENV}   ")
    assert instance is not None
    assert instance.environment_name is not None
    assert instance.environment_name == TEST_ENV

    another_instance = Environment(TEST_ENV)
    assert another_instance.environment_name == instance.environment_name


def test_constructor_with_ctor_param_white_space():
    instance = Environment(f"  {TEST_ENV}   ")
    assert instance is not None
    assert instance.environment_name is not None
    assert instance.environment_name == TEST_ENV

    another_instance = Environment(TEST_ENV)
    assert another_instance.environment_name == instance.environment_name


def test_constructor_without_ctor_param():
    instance = Environment()
    assert instance is not None
    env_var_configuration = os.getenv(ENVIRONMENT_VAR_NAME, None)

    if env_var_configuration is None:
        assert instance.environment_name == ENVIRONMENT_NAME_DEFAULT, "No constructor argument, without environment " \
                                                                      "setting should result in default environment."
    else:
        assert instance.environment_name == env_var_configuration, "No constructor argument, with environment " \
                                                                   "setting should result in name matching " \
                                                                   "the value of the environment setting"

    another_instance = Environment()
    assert another_instance.environment_name == instance.environment_name


def test_shared_environment():
    instance1 = Environment.get_default()
    instance2 = Environment.get_default()

    assert instance1 is not None
    assert instance2 is not None
    assert instance1.environment_name == instance2.environment_name
    assert instance2 is instance1, "Multiple calls to get_default() must result in the same instance."
