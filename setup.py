""" setup.py """
from distutils.core import setup

setup(
    name="bbtq",
    version="2.0.1",
    author="Andrew J. Erickson",
    author_email="aerickson@gmail.com",
    packages=["bbtq"],
    scripts=["bin/tq"],
    url="http://pypi.python.org/pypi/btq/",
    license="GPLv3",
    description="Barebones TOML query.",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=[
        "toml >= 0.10.0",
    ],
)
