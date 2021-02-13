import mapper
import pytest


def test_mapping_and_attrs():
    @mapper.set_attr("int_val", "int_val", int)
    @mapper.set_attr("string_val", "string_val", str)
    @mapper.set_attr("float_val", "float_val", float)
    @mapper.load_config("tests/mapper_test.yml")
    class TestClass:
        pass

    test_class = TestClass
    assert test_class.int_val == 2
    assert test_class.string_val == "Test String"
    assert test_class.float_val == 2.5


def test_load_config_fail():
    with pytest.raises(FileNotFoundError):
        @mapper.load_config("no_file.yml")
        class FailClass:
            pass


def test_key_mapping_fail():
    with pytest.raises(KeyError):
        @mapper.set_attr("test_attr", "missing_key", str)
        @mapper.load_config("tests/mapper_test.yml")
        class FailClass:
            pass


def test_type_conversion_fail():
    with pytest.raises(ValueError):
        @mapper.set_attr("string_val", "string_val", int)
        @mapper.load_config("tests/mapper_test.yml")
        class FailClass:
            pass
