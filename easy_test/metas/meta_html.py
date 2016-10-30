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

        # context_model_variable
        if contains_option(meta, 'context_model_variable'):
            if not isinstance(meta.context_model_variable, str):
                raise RuntimeError(
                    "Test class %s.%s doesn't set context_model_variable as a string " % (module, name)
                )