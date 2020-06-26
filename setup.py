from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="simple-env",
    packages=["simple_env"],
    package_dir={"simple_env": "simple_env"},
    package_data={"simple_env": ["__init__.py"]},
    version="0.2.1",
    description="Super Simple Processing of Environmental Variables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel J. Dufour",
    author_email="daniel.j.dufour@gmail.com",
    url="https://github.com/DanielJDufour/simple-env",
    download_url="https://github.com/DanielJDufour/simple-env/tarball/download",
    keywords=["env", "environment", "python", "variables"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
