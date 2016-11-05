import collections

from easy_test.metas.meta_html import HtmlMeta
from easy_test.util import contains_option


class FormMeta(HtmlMeta):

    def validate(cls, meta, module, name):
        super().validate(cls, meta, module, name)

        #form
        if not contains_option(meta, 'form'):
            raise RuntimeError(
                "Test class %s.%s doesn't set the form " % (module, name)
            )
