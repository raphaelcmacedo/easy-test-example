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

        #HtmlTest
        if contains_option(meta, 'url'):
            self.url = meta.url

        if contains_option(meta, 'url_arg_field'):
            self.url_arg_field = meta.url_arg_field

        if contains_option(meta, 'template'):
            self.template = meta.template

        if contains_option(meta, 'contents'):
            self.contents = meta.contents

        if contains_option(meta, 'context_variables'):
            self.context_variables = meta.context_variables

        if contains_option(meta, 'context_model_variable'):
            self.context_model_variable = meta.context_model_variable

        if contains_option(meta, 'ignore_csrfmiddlewaretoken'):
            self.ignore_csrfmiddlewaretoken = meta.ignore_csrfmiddlewaretoken
        else:
            self.ignore_csrfmiddlewaretoken = False

        #FormTest
        if contains_option(meta, 'form'):
            self.form = meta.form

        if contains_option(meta, 'ignore_form_errors'):
            self.ignore_form_errors = meta.ignore_form_errors
        else:
            self.ignore_form_errors = False
