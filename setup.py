from setuptools import setup, find_packages

# the best setup
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='datarec', packages=find_packages(), install_requires=requirements)
