import collections

from easy_test.metas.base import BaseMeta
from easy_test.util import contains_option, HttpMethods


class HtmlMeta(BaseMeta):

    def validate(cls, meta, module, name):
        super().validate(cls, meta, module, name)

        #url
        if not contains_option(meta, 'url'):
            raise RuntimeError(
                "Test class %s.%s doesn't set the url " % (module, name)
            )

        #method
        if contains_option(meta, 'method') and meta.method not in HttpMethods.__dict__.values():
            raise RuntimeError(
                "Test class %s.%s has set an invalid http method: %s. Please use the EasyTest class 'Method' to select an appropriate value." % (module, name, meta.method)
            )

        #status_code
        if contains_option(meta, 'status_code'):
            if not isinstance(meta.none_fields, int):
                raise RuntimeError(
                    "Test class %s.%s doesn't set none_fields as a int "
                    "value." % (module, name)
                )

        #contents
        if contains_option(meta, 'contents'):
            if not isinstance(meta.contents, collections.Sequence):
                raise RuntimeError(
                    "Test class %s.%s doesn't set contents as a sequence "
                    "instance." % (module, name)
                )

        #context_variables
        if contains_option(meta, 'context_variables'):
            if not isinstance(meta.context_variables, collections.Sequence):
                raise RuntimeError(
                    "Test class %s.%s doesn't set context_variables as a sequence "
                    "instance." % (module, name)
                )