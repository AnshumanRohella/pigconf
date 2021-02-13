# PIGCONF Configuration Mapper

---

Pigconf is a simple config mapper that maps yaml style configurations to configuration classes. It allows strict mapping
of yaml fields to class attributes based on specified keys.

## Installation 

Run the followint to install:

```bash
pip install pigconf
```

## Quickstart Example

student_conf.yml
```yaml
student:
  id: 1
  name: "Alice"
  info:
    grade: "A"
```
```python
import mapper

@mapper.set_attr("grade","student.info.grade", str)
@mapper.set_attr("name", "student.name", str)
@mapper.set_attr(attr_name="id", config_key="student.id", attr_type=int)
@mapper.load_config("student_conf.yml")
class Student:
    pass
```

```shell
>>> import mapper
>>> 
>>> 
>>> @mapper.set_attr("grade","student.info.grade", str)
... @mapper.set_attr("name", "student.name", str)
... @mapper.set_attr(attr_name="id", config_key="student.id", attr_type=int)
... @mapper.load_config("student_conf.yml")
... class Student:
...     pass
... 
>>> s = Student
>>> print(f"Student name: {s.name} with id: {s.id} has the grade: {s.grade}")
Student name: Alice with id: 1 has the grade: A

```

The configuration can also be loaded with a config_key argument so that the whole
object under that key is mapped. 

Example:

```python
import mapper

@mapper.set_attr("grade","info.grade", str)
@mapper.set_attr("name", "no_key", str)
@mapper.set_attr(attr_name="id", config_key="id", attr_type=int)
@mapper.load_config("student_conf.yml",config_key="student")
class Student:
    pass
```

Now the attributes only need the keys under defined under the "student" key in the yaml.

### Strict Mapping

The mapper doesn't allow None values or missing keys. Anything specified as an attribute 
key must be defined in the yaml. This simply allows the application to fail during the configuration 
mapping phase rather than failing at runtime.

```shell
>>> import mapper
>>> @mapper.set_attr("grade","info.wrong_key", str)
... @mapper.load_config("student_conf.yml","student")
... class Student:
...     pass
... 
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/Users/anshumanrohella/Documents/Workspace/pigconf/src/mapper.py", line 31, in decorator
    value = _get_value_from_parsed_config(cls._config, config_key)
  File "/Users/anshumanrohella/Documents/Workspace/pigconf/src/mapper.py", line 46, in _get_value_from_parsed_config
    raise KeyError(f"Could not find key: {key} in config file.")
KeyError: 'Could not find key: wrong_key in config file.'

```

## Contribute

To install pigconf, along with the tools you need to develop and run tests, run the following in your virtualenv.

```bash
pip install -e .[dev]
```
