import collections

from easy_test.metas.meta_html import HtmlMeta
from easy_test.util import contains_option


class DeleteMeta(HtmlMeta):

    def validate(cls, meta, module, name):
        super().validate(cls, meta, module, name)

        # url
        if not contains_option(meta, 'url'):
            raise RuntimeError(
                "Test class %s.%s doesn't set the url " % (module, name)
            )
