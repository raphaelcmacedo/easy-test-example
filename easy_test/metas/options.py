from easy_test.util import contains_option


class Options(object):

    def __init__(self, meta):
        self.obj = meta.obj
        self.model = self.obj.__class__

        #ModelTest
        if contains_option(meta, 'blank_fields'):
            self.blank_fields = meta.blank_fields

        if contains_option(meta, 'none_fields'):
            self.none_fields = meta.none_fields

        if contains_option(meta, 'string'):
            self.string = meta.string

        if contains_option(meta, 'ordering'):
            self.ordering = meta.ordering

        #HtmlList
        if contains_option(meta, 'url'):
            self.url = meta.url

        if contains_option(meta, 'method'):
            self.method = meta.method

        if contains_option(meta, 'status_code'):
            self.status_code = meta.status_code

        if contains_option(meta, 'template'):
            self.template = meta.template

        if contains_option(meta, 'contents'):
            self.contents = meta.contents

        if contains_option(meta, 'context_variables'):
            self.context_variables = meta.context_variables
