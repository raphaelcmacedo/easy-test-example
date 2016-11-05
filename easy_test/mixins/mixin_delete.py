from easy_test.mixins.mixin_html import HtmlMixin

class GetDeleteMixin():

    def test_get(self):
        if not self._concrete:
            return

        self.assertEqual(self.response.status_code, 200)


class PostDeleteMixin():
    def test_redirect(self):
        if not self._concrete:
            return

        self.assertEqual(self.response_post.status_code, 302)

    def test_exists(self):
        if not self._concrete:
            return

        self.assertFalse(self._meta.model.objects.filter(pk = self._meta.obj.pk))


class DeleteMixin(GetDeleteMixin, PostDeleteMixin, HtmlMixin):
    pass




