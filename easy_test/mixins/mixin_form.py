from easy_test.mixins.mixin_html import HtmlMixin

class ValidFormMixin():

    def test_save_subscription(self):
        if not self._concrete:
            return

        self.assertTrue(self._meta.model.objects.exists())


class InvalidFormMixin():
    def test_has_erros(self):
        if not self._concrete:
            return

        if self._meta.ignore_form_errors:
            return

        form = self.responseInvalid.context['form']
        self.assertTrue(form.errors)

    def test_not_save_subscription(self):
        if not self._concrete:
            return

        self.assertEqual(len(self._meta.model.objects.all()), 1)


class FormMixin(ValidFormMixin, InvalidFormMixin, HtmlMixin):
    def test_has_form(self):
        if not self._concrete:
            return

        form = self.response.context['form']
        self.assertIsInstance(form,self._meta.form)



