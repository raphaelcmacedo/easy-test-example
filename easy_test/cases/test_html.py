from django.shortcuts import resolve_url
from django.test import TestCase

from easy_test.metas.meta_html import HtmlMeta
from easy_test.mixins.mixin_html import HtmlMixin
from easy_test.util import contains_option


class HtmlTest(TestCase,HtmlMixin, metaclass=HtmlMeta):
    def setUp(self):
        if not self._concrete:
            return

        self._meta.obj.save()
        self.status_code = 200

        if contains_option(self._meta, 'url_arg_field'):
            arg = getattr(self._meta.obj, self._meta.url_arg_field, '')
            self.response = self.client.get(resolve_url(self._meta.url,arg))
        else:
            self.response = self.client.get(resolve_url(self._meta.url))

    def test_not_found(self):
        if not self._concrete:
            return
        if contains_option(self._meta, 'url_arg_field'):
            self.response = self.client.get(resolve_url(self._meta.url, 0))
            self.assertEqual(self.response.status_code, 404)


