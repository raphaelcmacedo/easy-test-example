from django.test import TestCase

from easy_test.metas.meta_html import HtmlMeta
from easy_test.util import contains_option, HttpMethods


class HtmlTest(TestCase, metaclass=HtmlMeta):
    def setUp(self):
        if not self._concrete:
            return
        self.obj = self._meta.obj.save()

        method = HttpMethods.GET
        if contains_option(self._meta, 'method'):
            method = self._meta.method

        if method == HttpMethods.GET:
            self.response = self.client.get(self._meta.url)
        elif method == HttpMethods.POST:
            self.response = self.client.post(self._meta.url)
        elif method == HttpMethods.PUT:
            self.response = self.client.put(self._meta.url)
        elif method == HttpMethods.DELETE:
            self.response = self.client.delete(self._meta.url)

    def test_status_code(self):
        if not self._concrete:
            return

        status_code = 200
        if contains_option(self._meta, 'status_code'):
            status_code = self._meta.status_code

        self.assertEqual(status_code, self.response.status_code)

    def test_template(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'template'):
            return

        template = self._meta.template
        self.assertTemplateUsed(self.response, template)

    def test_content(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'contents'):
            return
        contents = self._meta.contents

        # Verify if was informed one or more fields
        if isinstance(contents, str):
            self.assertContains(self.response, contents)
        else:
            for content in contents:
                with self.subTest():
                    self.assertContains(self.response, content)
                    
    def test_context(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'context_variables'):
            return
        variables = self._meta.context_variables

        # Verify if was informed one or more fields
        if isinstance(variables, str):
            self.assertIn(variables, self.response.context)
        else:
            for variable in variables:
                with self.subTest():
                    self.assertIn(variable, self.response.context)
