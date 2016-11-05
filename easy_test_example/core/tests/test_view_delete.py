from django.test import TestCase
from django.shortcuts import resolve_url

from easy_test.cases.test_delete import DeleteTest
from easy_test_example.core.models import Task

class TaskDeleteGet(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )

        self.response = self.client.get(resolve_url('task_delete', self.task.pk))

    def test_redirect(self):
        self.assertEqual(self.response.status_code,200)

    def test_html(self):
        tags = (
            ('<form',1),
            ('<input', 2),
            ('type="submit"', 1),
            (str(self.task), 1),
            ('Are you sure you want to delete', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

class TaskDeletePost(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )

        self.response = self.client.post(resolve_url('task_delete', self.task.pk))

    def test_redirect(self):
        self.assertEqual(self.response.status_code,302)

    def test_exists(self):
        self.assertFalse(Task.objects.filter(pk = self.task.pk))


class TaskDeleteEasyTest(DeleteTest):
    class Meta:
        obj = Task(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )
        url = 'task_delete'
        contents = [
            ('<form',1),
            ('<input', 2),
            ('type="submit"', 1),
            (str(obj), 1),
            ('Are you sure you want to delete', 1)
        ]




