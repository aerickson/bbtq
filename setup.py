from distutils.core import setup

setup(
    name='btq',
    version='0.1.0',
    author='Andrew J. Erickson',
    author_email='aerickson@gmail.com',
    packages=['btq'],
    scripts=['bin/tq'],
    url='http://pypi.python.org/pypi/btq/',
    license='GPLv3',
    description='Useful towel-related stuff.',
    long_description=open('README.md').read(),
    install_requires=[
        "toml >= 0.10.0",
    ],
)
