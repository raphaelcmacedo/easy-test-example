from django.shortcuts import resolve_url
from django.test import TestCase

from easy_test.metas.meta_delete import DeleteMeta
from easy_test.mixins.mixin_delete import DeleteMixin


class DeleteTest(TestCase,DeleteMixin, metaclass=DeleteMeta):
    def setUp(self):
        if not self._concrete:
            return

        self._meta.obj.save()
        self.status_code = 200

        self.response = self.client.get(resolve_url(self._meta.url, self._meta.obj.pk))
        self.response_post = self.client.post(resolve_url(self._meta.url, self._meta.obj.pk))






