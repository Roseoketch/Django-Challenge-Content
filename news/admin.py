from django.contrib import admin

# Register your models here.
from .models import Editor,Article,tag

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tag)