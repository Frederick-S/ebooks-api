from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='ebooks',
    version='0.0.1',
    description='Search ebooks from various sites.',
    url='https://github.com/Frederick-S/ebooks',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    test_suite="tests"
)
