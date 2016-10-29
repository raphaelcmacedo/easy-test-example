from django.test import TestCase

from easy_test.metas.meta_model import ModelMeta
from easy_test.util import contains_option


class ModelTest(TestCase, metaclass=ModelMeta):
    def setUp(self):
        if not self._concrete:
            return
        self.obj = self._meta.obj.save()

    def test_create(self):
        if not self._concrete:
            return
        self.assertTrue(self._meta.model.objects.exists())

    def test_blank(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'blank_fields'):
            return
        blank_fields = self._meta.blank_fields

        # Verify if was informed one or more fields
        if isinstance(blank_fields, str):
            self.field_is_blank(blank_fields)
        else:
            for blank_field in blank_fields:
                with self.subTest:
                    self.field_is_blank(blank_field)
                    
    def test_none(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'none_fields'):
            return
        none_fields = self._meta.none_fields

        # Verify if was informed one or more fields
        if isinstance(none_fields, str):
            self.field_is_none(none_fields)
        else:
            for none_field in none_fields:
                with self.subTest:
                    self.field_is_none(none_field)

    def test_str(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'string'):
            return
        string = self._meta.string

        self.assertEqual(string, str(self._meta.obj))

    def test_ordering(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'ordering'):
            return
        ordering = self._meta.ordering

        self.assertListEqual(ordering, list(self._meta.model._meta.ordering))

    def get_field(self, model, field_name):
        return model._meta.get_field(field_name)

    def field_is_blank(self, field_name):
        field = self.get_field(self._meta.model, field_name)
        self.assertTrue(field.blank)

    def field_is_none(self, field_name):
        field = self.get_field(self._meta.model, field_name)
        self.assertTrue(field.none)
