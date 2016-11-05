from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase

from easy_test.cases.test_form import FormTest
from easy_test_example.core.forms import TaskForm
from easy_test_example.core.models import Task


class TaskNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('task_new'))

    def test_html(self):
        tags = (
            ('<form',1),
            ('<input', 3),
            ('<textarea', 1),
            ('type="text"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,TaskForm)


class TaskNewPostValid(TestCase):
    def setUp(self):
        data = dict(name='Easy Test', description='')
        self.response = self.client.post(resolve_url('task_new'), data)

    def test_save_subscription(self):
        self.assertTrue(Task.objects.exists())


class TaskNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(resolve_url('task_new'),{})

    def test_post(self):
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "core/task_form.html")

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form,TaskForm)

    def test_has_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_not_save_subscription(self):
        self.assertFalse(Task.objects.exists())

class TaskFormEasyTest(FormTest):
    class Meta:
        obj = Task(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )
        url = 'task_new'
        template = 'core/task_form.html'
        contents = [
            ('<form',1),
            ('<input', 3),
            ('<textarea', 1),
            ('type="text"', 1),
            ('type="submit"', 1)
        ]
        form = TaskForm