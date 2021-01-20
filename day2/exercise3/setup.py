from setuptools import setup, find_packages


setup(
    name='mymath',
    version='0.1',
    description='Tutorial package for CURP',
    author='Wenda Zhou',
    packages=find_packages('src'),
    package_dir={
        '': 'src'
    }
)
