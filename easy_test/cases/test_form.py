from django.shortcuts import resolve_url
from django.test import TestCase

from easy_test.metas.meta_html import HtmlMeta
from easy_test.mixins.mixin_form import FormMixin
from easy_test.mixins.mixin_html import HtmlMixin
from easy_test.util import contains_option


class FormTest(TestCase,FormMixin, metaclass=HtmlMeta):
    def setUp(self):
        if not self._concrete:
            return

        data = self._meta.obj.__dict__
        self.status_code = 200
        self.response = self.client.get(resolve_url(self._meta.url))
        self.responseValid = self.client.post(resolve_url(self._meta.url), data)
        self.responseInvalid = self.client.post(resolve_url(self._meta.url), {})






