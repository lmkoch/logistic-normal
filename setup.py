__author__ = 'lkoch'

from setuptools import setup, find_packages


setup(
    # Application name:
    name='logisticnormal',

    description='Logistic-normal distribution: provides probability density function and parameter estimation',

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author='Lisa Koch',
    author_email='l.koch@imperial.ac.uk',

    # Packages
    packages=['logisticnormal'],

    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",
    download_url="http://pypi.python.org/pypi/MyApplication_v010/",

    #
    license='MIT',

    install_requires = [
        'scipy >= 0.10.1',
        'numpy >= 1.6.2'
    ],

    # long_description=open("README.txt").read(),
)