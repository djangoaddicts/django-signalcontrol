import os
from setuptools import setup, find_packages
import userextensions

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-userextensions',
    packages=find_packages(),
    include_package_data=True,
    version=userextensions.__version__,
    license=userextensions.__license__,
    author='David Slusser',
    author_email='dbslusser@gmail.com',
    description='A user extension module for django',
    #long_description=README,
    url='https://github.com/davidslusser/django-userextensions',
    download_url='https://github.com/davidslusser/django-userextensions/archive/0.0.2.tar.gz',
    keywords=['django', 'helpers', 'extension', 'user', 'profile'],
    classifiers=[],
    install_requires=[
        'django',
        'django-handyhelpers',
    ],
    dependency_links=[],
)
