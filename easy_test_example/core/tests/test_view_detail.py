from django.test import TestCase
from django.shortcuts import resolve_url

from easy_test_example.core.models import Task


class TaskDetailGet(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )

        self.response = self.client.get(resolve_url('task_detail', self.task.pk))

    def test_get(self):
        self.assertEqual(self.response.status_code,200)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'core/task_form.html')

    def test_context(self):
        task = self.response.context['task']
        self.assertIsInstance(task, Task)

    def test_html(self):
        values = (self.task.name, self.task.description)
        for value in values:
            with self.subTest():
                self.assertContains(self.response, value)


class TaskDetailNotFound(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('task_detail',0))

    def test_not_found(self):
        self.assertEqual(self.response.status_code, 404)
