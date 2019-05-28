from django.db.models.signals import post_save
from django.dispatch import receiver
import sys

# import models
from userprofile.models import UserRecent


@receiver(post_save, sender=UserRecent, dispatch_uid="trim_recents")
def trim_recents(sender, instance, created, **kwargs):
    """ trim the recents list for a user to only maintain the (10) most recent urls """
    # do not execute signal when running tests
    if 'manage.py' in sys.argv[0] and 'test' in sys.argv:
        return

    # get recents count from user preferences if available; else default to 25
    try:
        recents_count = instance.user.preference.recents_count
    except:
        recents_count = 25

    # don't need to trip if recents count is < 10
    if UserRecent.objects.filter(user=instance.user).count() <= recents_count:
        return
    recent_id_list = UserRecent.objects.filter(user=instance.user
                                               ).order_by('-updated_at')[:recents_count].values_list("id", flat=True)
    UserRecent.objects.filter(user=instance.user).exclude(pk__in=list(recent_id_list)).delete()
