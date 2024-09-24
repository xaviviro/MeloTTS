import os 
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


cwd = os.path.dirname(os.path.abspath(__file__))

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        os.system('python -m unidic download')


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        os.system('python -m unidic download')

setup(
    name='melotts',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    package_data={
        '': ['*.txt', 'cmudict_*'],
    },
    dependency_links=[
        'git+https://github.com/xaviviro/num2words.git'
    ],
    entry_points={
        "console_scripts": [
            "melotts = melo.main:main",
            "melo = melo.main:main",
            "melo-ui = melo.app:main",
        ],
    },
)
