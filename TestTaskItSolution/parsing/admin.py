from django.contrib import admin

from django.contrib import admin

from . models import *


@admin.register(Advert)
class Advert(admin.ModelAdmin):
    list_display = ('id', 'title', 'reference_id', 'author', 'views_count', 'position')
    list_filter = ('title', )