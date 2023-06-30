import importlib
import random
from django.apps import apps
from django.conf import settings
from django.test import TestCase
from model_bakery import baker
import sys
from io import StringIO

from unittest.mock import patch
from django.contrib.auth.models import User

from djangoaddicts.signalcontrol.decorators import find_app_name, init_signal_control
import tests.core.testapp.signals


class SignalControlTests(TestCase):
    """test SignalControl decorator and helper functions"""
    def setUp(self):
        importlib.reload(tests.core.testapp.signals)
        self.model = apps.get_model("signalcontrol.SignalControl")

    def test_invalid_file(self):
        """verify app can not be determined if invalid file provided"""
        resp = find_app_name("no_file", "no_signal")
        self.assertEqual(1, resp)
    
    def test_signal_register(self):
        """verify model signal is found and added to SignalControl"""
        self.assertEqual(2, self.model.objects.count())
    
    def test_model_signal_trigger_enabled(self):
        """verify model signal is triggered if signal is enabled"""
        expected_output = "SIGNAL: you just saved an instance of TestModel"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        baker.make("testapp.TestModel")
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, capturedOutput.getvalue().strip())

    def test_model_signal_trigger_disabled(self):
        """verify model signal is not triggered if signal is disabled"""
        self.model.objects.update(enabled=False)
        expected_output = "SIGNAL: you just saved an instance of TestModel"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        baker.make("testapp.TestModel")
        sys.stdout = sys.__stdout__
        self.assertNotEqual(expected_output, capturedOutput.getvalue().strip())

    def test_non_model_signal_trigger_enabled(self):
        """verify non-model signal is triggered if signal is enabled"""
        user = User.objects.create_user(username="user", password="user")
        expected_output = f"SIGNAL: login successful for user: {user}"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.client.force_login(user)
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, capturedOutput.getvalue().strip())

    def test_non_model_signal_trigger_disabled(self):
        """verify non-model signal is not triggered if signal is disabled"""
        self.model.objects.update(enabled=False)
        user = User.objects.create_user(username="user", password="user")
        expected_output = f"SIGNAL: login successful for user: {user}"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.client.force_login(user)
        sys.stdout = sys.__stdout__
        self.assertNotEqual(expected_output, capturedOutput.getvalue().strip())
