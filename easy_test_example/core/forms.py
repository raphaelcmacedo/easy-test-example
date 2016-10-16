from django import forms
from django.core.exceptions import ValidationError

from easy_test_example.core.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description']


