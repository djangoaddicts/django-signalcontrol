import logging

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver

from djangoaddicts.signalcontrol.decorators import signal_control


# import models
from .models import TestModel

user_logger = logging.getLogger('user')


# method for updating
@receiver(post_save, sender=TestModel)
@signal_control
def test_model(sender, instance, created, **kwargs):
    print('SIGNAL: you just saved an instance of TestModel')


# log user login succeeded
@receiver(user_logged_in)
@signal_control
def log_user_login(sender, user, request, **kwargs):
    """ log user login to user log """
    print(f'SIGNAL: login successful for user: {user}')
