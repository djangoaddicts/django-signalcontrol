from django.apps import apps
from django.test import TestCase
from model_bakery import baker


class SignalControlTests(TestCase):
    """test SignalControl model methods"""
    def setUp(self):
        self.model = apps.get_model("signalcontrol", "signalcontrol")
        self.to_bake = "signalcontrol.SignalControl"
        self.signal_name = "this is a test"

    def bake(self):
        """add row"""
        return baker.make(self.to_bake, signal_name=self.signal_name)

    def test_str(self):
        """verify __str__() method of SignalControl model returns expected value"""
        row = self.bake()
        self.assertTrue(isinstance(row, self.model))
        self.assertEqual(row.__str__(), self.signal_name)

    def test_unicode(self):
        """verify __unicode__() method of SignalControl model returns expected value"""
        row = self.bake()
        self.assertTrue(isinstance(row, self.model))
        self.assertEqual(row.__unicode__(), self.signal_name)
