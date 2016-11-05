from easy_test.util import contains_option


class HtmlMixin():
    def test_status_code(self):
        if not self._concrete:
            return

        self.assertEqual(self.status_code, self.response.status_code)

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
        if len(contents) <= 0:
            return

        # Verify if was informed one or more fields
        if isinstance(contents, str):
            self.assertContains(self.response, contents)
        elif isinstance(contents[0], tuple):
            for content, count in contents:
                with self.subTest():
                    self.assertContains(self.response, content, count)
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

    def test_model_context(self):
        if not self._concrete:
            return
        if not contains_option(self._meta, 'context_model_variable'):
            return

        context_model_variable = self._meta.context_model_variable
        self.assertIn(context_model_variable, self.response.context)

        variable = self.response.context[context_model_variable]
        self.assertIsInstance(variable, self._meta.model)

    def test_csrf(self):
        if not self._concrete:
            return

        if self._meta.ignore_csrfmiddlewaretoken:
            return

        self.assertContains(self.response, 'csrfmiddlewaretoken')
