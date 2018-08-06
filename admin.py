# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import question,topics,chapter

# Register your models here.
admin.site.register(chapter)
admin.site.register(topics)
admin.site.register(question)
