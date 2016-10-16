"""easy_test_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from easy_test_example.core.views import home, task_detail, task_new, task_delete

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^task/$', task_new, name='task_new'),
    url(r'^task/(?P<pk>[\d-]+)/$', task_detail, name='task_detail'),
    url(r'^task_delete/(?P<pk>[\d-]+)/$', task_delete, name='task_delete'),
    url(r'^admin/', admin.site.urls),
]
