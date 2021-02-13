from setuptools import setup

setup(
    name='pigconf',
    version='0.0.1',
    descriptoion='A yaml config mapper to create static config classes.',
    py_modules=["mapper"],
    package_dir={'': "src"},
    install_requires=["PyYAML>=5.4.1"],
)
