from django.db import models
from django.shortcuts import resolve_url


class Task (models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('task_detail',self.pk)

    def get_delete_url(self):
        return resolve_url('task_delete',self.pk)
