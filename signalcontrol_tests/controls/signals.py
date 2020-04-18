from django.db.models.signals import (post_save)
from django.dispatch import receiver
from .decorators import signal_control

# import models
from .models import (MyModelOne, MyModelTwo, MyModelThree)


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
def msg_my_model_four(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelThree; blah")