from django.contrib import admin
from core.models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin): pass