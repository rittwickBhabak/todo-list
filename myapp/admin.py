from django.contrib import admin
from .models import ToDo, CompletedToDo

admin.site.register(ToDo)
admin.site.register(CompletedToDo)