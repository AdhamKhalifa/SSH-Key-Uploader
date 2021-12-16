# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

class TodolistConfig(AppConfig):
    name = 'todolist'