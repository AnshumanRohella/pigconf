from setuptools import setup


setup(
    name='pigconf',
    version='0.0.1',
    author="Anshuman Rohella",
    author_email="rohella.anshuman@gmail.com",
    descriptoion='A yaml config mapper to create static config classes.',
    py_modules=["mapper"],
    package_dir={'': "src"},
    install_requires=["PyYAML>=5.4.1"],
    extra_require={
        "dev": [
            "pytest>=6.2.2",
        ],
    },
)
