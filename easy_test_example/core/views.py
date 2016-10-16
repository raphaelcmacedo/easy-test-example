from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from easy_test_example.core.forms import TaskForm
from easy_test_example.core.models import Task

home = ListView.as_view(template_name='index.html', model=Task)
task_new = CreateView.as_view(model=Task, form_class=TaskForm, success_url = reverse_lazy('home'))
task_detail = UpdateView.as_view(model=Task, form_class=TaskForm, success_url = reverse_lazy('home'))
task_delete = DeleteView.as_view(model=Task, success_url = reverse_lazy('home'))