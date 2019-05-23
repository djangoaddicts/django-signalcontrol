import os
from setuptools import setup, find_packages
import userprofile

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-userprofile',
    packages=find_packages(),
    include_package_data=True,
    version=userprofile.__version__,
    license=userprofile.__license__,
    author='David Slusser',
    author_email='dbslusser@gmail.com',
    description='A user profile module for django',
    long_description=README,
    url='https://github.com/davidslusser/django-userprofile',
    download_url='',
    keywords=['django', 'helpers', 'user', 'profile'],
    classifiers=[],
    install_requires=[
        'django',
        'django-handyhelpers',
    ],
    dependency_links=[],
)
