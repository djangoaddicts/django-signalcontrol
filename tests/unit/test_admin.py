from django.apps import apps
from django.test import TestCase
from model_bakery import baker

from django.contrib.admin.sites import AdminSite
from django.contrib.admin.options import ModelAdmin
from django.shortcuts import reverse
from django.contrib.auth.models import User

from djangoaddicts.signalcontrol.models import SignalControl


class MockRequest:
    pass


class ModelAdminTests(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.model = apps.get_model("signalcontrol", "signalcontrol")
        self.request = MockRequest()
        self.field_list = ["app_name", "model_name", "signal_name", "signal_type", "enabled"]

    def test_modeladmin_str(self):
        ma = ModelAdmin(self.model, self.site)
        self.assertEqual(str(ma), "signalcontrol.ModelAdmin")

    def test_default_attributes(self):
        ma = ModelAdmin(self.model, self.site)
        self.assertEqual(ma.actions, ())
        self.assertEqual(ma.inlines, ())

    def test_default_fields(self):
        ma = ModelAdmin(self.model, self.site)
        self.assertEqual(list(ma.get_form(self.request).base_fields), self.field_list)
        self.assertEqual(list(ma.get_fields(self.request)), self.field_list)
        self.assertEqual(list(ma.get_fields(self.request, self.model)), self.field_list)
        self.assertIsNone(ma.get_exclude(self.request, self.model))

    def test_action_disable(self):
        url = reverse("admin:signalcontrol_signalcontrol_changelist")
        row1 = baker.make("signalcontrol.SignalControl")
        row2 = baker.make("signalcontrol.SignalControl")
        data = {"action": "disable", "_selected_action": [row1.id, row2.id]}
        superuser = User.objects.create_superuser(username="superuser", password="superuser", is_staff=True)
        self.client.force_login(superuser)
        response = self.client.post(url, data, follow=True)
        self.client.logout()
        self.assertEqual(response.status_code, 200)
        updated1 = SignalControl.objects.get(id=row1.id)
        updated2 = SignalControl.objects.get(id=row2.id)
        self.assertFalse(updated1.enabled)
        self.assertFalse(updated2.enabled)

    def test_action_enable(self):
        url = reverse("admin:signalcontrol_signalcontrol_changelist")
        row1 = baker.make("signalcontrol.SignalControl", enabled=False)
        row2 = baker.make("signalcontrol.SignalControl", enabled=False)
        data = {"action": "enable", "_selected_action": [row1.id, row2.id]}
        superuser = User.objects.create_superuser(username="superuser", password="superuser", is_staff=True)
        self.client.force_login(superuser)
        response = self.client.post(url, data, follow=True)
        self.client.logout()
        self.assertEqual(response.status_code, 200)
        updated1 = SignalControl.objects.get(id=row1.id)
        updated2 = SignalControl.objects.get(id=row2.id)
        self.assertTrue(updated1.enabled)
        self.assertTrue(updated2.enabled)
