from django.db import models


class SignalControl(models.Model):
    """ table to track status of a signal used in the signal_control decorator """
    app_name = models.CharField(max_length=32)
    model_name = models.CharField(max_length=128)
    signal_name = models.CharField(max_length=255)
    signal_type = models.CharField(max_length=32)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = "signalcontrol"
        unique_together = (('app_name', 'model_name', 'signal_name'), )

    def __unicode__(self):
        return u'%s' % self.signal_name

    def __str__(self):
        return self.signal_name
