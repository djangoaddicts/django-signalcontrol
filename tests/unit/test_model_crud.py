import random
from django.apps import apps
from django.test import TestCase
from model_bakery import baker


class SignalControlTests(TestCase):
    """test CRUD operations on SignalControl"""
    def setUp(self):
        self.model = apps.get_model("signalcontrol", "signalcontrol")
        self.to_bake = "signalcontrol.SignalControl"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(id=row.id)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.id, entry.id)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_id = row.id
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(id=row_id)
        self.assertLess(after_count, before_count)

    def test_update_app_name(self):
        """verify app_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.app_name
        choices = getattr(self.model.app_name.field, "choices", None)
        if choices:
            updated_value = random.choice([i[0] for i in choices if original_value not in i])
        else:
            updated_value = baker.prepare(self.to_bake, _fill_optional=["app_name"]).app_name
        setattr(row, "app_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "app_name"), updated_value)
        self.assertNotEqual(getattr(row, "app_name"), original_value)

    def test_update_model_name(self):
        """verify model_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.model_name
        choices = getattr(self.model.model_name.field, "choices", None)
        if choices:
            updated_value = random.choice([i[0] for i in choices if original_value not in i])
        else:
            updated_value = baker.prepare(self.to_bake, _fill_optional=["model_name"]).model_name
        setattr(row, "model_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "model_name"), updated_value)
        self.assertNotEqual(getattr(row, "model_name"), original_value)

    def test_update_signal_name(self):
        """verify signal_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.signal_name
        choices = getattr(self.model.signal_name.field, "choices", None)
        if choices:
            updated_value = random.choice([i[0] for i in choices if original_value not in i])
        else:
            updated_value = baker.prepare(self.to_bake, _fill_optional=["signal_name"]).signal_name
        setattr(row, "signal_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "signal_name"), updated_value)
        self.assertNotEqual(getattr(row, "signal_name"), original_value)

    def test_update_signal_type(self):
        """verify signal_type (CharField) can be updated"""
        row = self.bake()
        original_value = row.signal_type
        choices = getattr(self.model.signal_type.field, "choices", None)
        if choices:
            updated_value = random.choice([i[0] for i in choices if original_value not in i])
        else:
            updated_value = baker.prepare(self.to_bake, _fill_optional=["signal_type"]).signal_type
        setattr(row, "signal_type", updated_value)
        row.save()
        self.assertEqual(getattr(row, "signal_type"), updated_value)
        self.assertNotEqual(getattr(row, "signal_type"), original_value)
