import os
from setuptools import setup
from src import signalcontrol

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

version = signalcontrol.__version__

setup(
    name='django-signalcontrol',
    description='A django app to allow dynamic control of signals',
    long_description=README,
    long_description_content_type='text/markdown',
    packages=['signalcontrol', 'signalcontrol.migrations'],
    package_dir={'': 'src'},
    version=version,
    license=signalcontrol.__license__,
    author=signalcontrol.__author__,
    author_email=signalcontrol.__email__,
    url='https://github.com/davidslusser/django-signalcontrol',
    download_url='https://github.com/davidslusser/django-signalcontrol/archive/{}.tar.gz'.format(version),
    keywords=['django', 'helpers', 'signal', 'control', 'admin'],
    install_requires=required,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 2.2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
