from setuptools import setup, find_packages

requires = [
    'Flask==1.1.1',
    'requests==2.23.0'
]

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
