#!/usr/bin/env python

# import system modules
import sys
import os
import datetime
import argparse
import string
import random
import logging
import django
import environ
from django.db.models import signals

# setup django
sys.path.append(str(environ.Path(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "signalcontrol_tests.settings")
django.setup()

__version__ = "0.0.1"

# import models


def get_opts():
    """ Return an argparse object. """
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--verbose", default=logging.INFO, action="store_const",
                        const=logging.DEBUG, help="enable debug logging")
    parser.add_argument("--version", action="version", version=__version__, help="show version and exit")
    parser.add_argument("--clean", action="store_true", required=False, help="delete existing records first")
    parser.add_argument("--disable_signals", action="store_true", required=False, help="disable django signals")
    args = parser.parse_args()
    logging.basicConfig(level=args.verbose)
    return args


def dec1(func):
    def func_wrapper(*args, **kwargs):
        print('in dec1')
        return func(*args, **kwargs)
    return func_wrapper


def dec2(func):
    def func_wrapper(*args, **kwargs):
        print('in dec2')
        return func(*args, **kwargs)
    return func_wrapper


def dec3(func):
    def func_wrapper(*args, **kwargs):
        print('in dec3')
        return func(*args, **kwargs)
    return func_wrapper


@dec1
@dec2
@dec3
def print_test(msg):
    print('this is the print test: {}'.format(msg))


def test_decs():
    """ """
    print_test('hello world')


def main():
    """ script entry point """
    opts = get_opts()
    logging.info("Starting script")
    start_time = datetime.datetime.now()

    test_decs()

    end_time = datetime.datetime.now() - start_time
    logging.info("")
    logging.info("Script completed in: %s", end_time)


if __name__ == "__main__":
    sys.exit(main())
