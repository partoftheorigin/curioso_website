# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Category
from home.models import Feedback, Writeforus

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

class Meta:
    model = Category

admin.site.register(Category, CategoryAdmin)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

class Meta:
    model = Post

admin.site.register(Post, PostModelAdmin)

admin.site.register(Feedback)

admin.site.register(Writeforus)
