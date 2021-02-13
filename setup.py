from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pigconf',
    version='0.0.3',
    author="Anshuman Rohella",
    author_email="rohella.anshuman@gmail.com",
    description='A yaml config mapper to create static config classes.',
    url="https://github.com/AnshumanRohella/pigconf",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['PyYAML>=5.4.1'],
    extras_require={
        "dev": [
            "pytest>=6.2.2",
            "check-manifest>=0.46"
        ],
    },
)
