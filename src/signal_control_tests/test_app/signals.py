from django.db.models.signals import (post_save)
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.conf import settings
import logging

# import models
from .models import (MyModelOne, MyModelTwo, MyModelThree)

# import local signalcontrol
from signalcontrol.decorators import signal_control


@receiver(post_save, sender=MyModelOne)
@signal_control
def msg_my_model_one(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelOne")


@receiver(post_save, sender=MyModelTwo)
@signal_control
def msg_my_model_two(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelTwo")


@receiver(post_save, sender=MyModelThree)
@signal_control
def msg_my_model_three(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelThree")


@receiver(post_save, sender=MyModelThree)
def msg_my_model_three_blah(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelThree; blah")


# if settings.LOGGING and \
#         'handlers' in settings.LOGGING.keys() and \
#         'user' in settings.LOGGING['handlers'].keys():
#     user_logger = logging.getLogger("user")
#
#     # log user login succeeded
#     @receiver(user_logged_in)
#     @signal_control
#     def log_user_login(sender, user, **kwargs):
#         """ log user login to user log """
#         user_logger.info('%s login successful', user)
#
#     # log user login failed
#     @receiver(user_login_failed)
#     @signal_control
#     def log_user_login_failed(sender, user=None, **kwargs):
#         """ log user login to user log """
#         if not user and hasattr(kwargs['credentials'], 'username'):
#             user = kwargs['credentials']['username']
#         if user:
#             user_logger.info('failed login attempt for user {}'.format(user))
#         else:
#             user_logger.info('login failed; unknown user')
#
#     # log user logout
#     @receiver(user_logged_out)
#     @signal_control
#     def log_user_logout(sender, user, **kwargs):
#         """ log user logout to user log """
#         user_logger.info('%s log out successful', user)
