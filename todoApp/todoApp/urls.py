# pages_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView

from django.conf.urls import *
from pages import views

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

#new
from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


urlpatterns = [
path('accounts/', include('accounts.urls')),
path('accounts/', include('django.contrib.auth.urls')),
#path('', TemplateView.as_view(template_name='home.html'), name='home'),
path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
path('completed/', TemplateView.as_view(template_name='completed.html'), name='completed'),
path('categories/', TemplateView.as_view(template_name='categories.html'), name='categories'),
path(r'^$', views.index, name="TodoList"),
path('', include('pages.urls')), # new
]