from django.shortcuts import resolve_url
from django.test import TestCase

from easy_test.cases.test_html import HtmlTest
from easy_test_example.core.models import Task


class ListGet(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name = 'Easy Test',
            description = 'A unit test framework for Django that will make your unit tests as easy as it should be.'
        )

        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        contents = [
            'Tasks',
            'Easy Test',
            'A unit test framework for Django that will make your unit tests as easy as it should be.'
        ]

        with self.subTest():
            for content in contents:
                with self.subTest():
                    self.assertContains(self.response, content)

    def test_context(self):
        variables = ['task_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)


class ListGetEasyTest(HtmlTest):
    class Meta:
        obj = Task(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )
        url = 'home'
        template = 'index.html'
        contents = [
            'Tasks',
            'Easy Test',
            'A unit test framework for Django that will make your unit tests as easy as it should be.'
        ]
        context_variables = ['task_list']
        ignore_csrfmiddlewaretoken = True

