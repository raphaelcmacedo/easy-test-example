from django.test import TestCase

from easy_test.cases.test_model import ModelTest
from easy_test_example.core.models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )

    def test_create(self):
        self.assertTrue(Task.objects.exists())

    def test_description_blank(self):
        field = Task._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Easy Test', str(self.task))

    def test_ordering(self):
        self.assertListEqual(['-created_at'], list(Task._meta.ordering))


class TaskModelEasyTest(ModelTest):
    class Meta:
        obj = Task(
            name='Easy Test',
            description='A unit test framework for Django that will make your unit tests as easy as it should be.'
        )
        blank_fields = 'description'
        string = 'Easy Test'
        ordering = ['-created_at']
