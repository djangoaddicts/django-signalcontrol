import os
from setuptools import setup, find_packages
import userextensions

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

version = userextensions.__version__

setup(
    name='django-userextensions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    license=userextensions.__license__,
    author='David Slusser',
    author_email='dbslusser@gmail.com',
    description='A user extension module for django',
    url='https://github.com/davidslusser/django-userextensions',
    download_url='https://github.com/davidslusser/django-userextensions/archive/{}.tar.gz'.format(version),
    keywords=['django', 'helpers', 'extension', 'user', 'profile'],
    classifiers=[],
    install_requires=required,
    dependency_links=[],
)
