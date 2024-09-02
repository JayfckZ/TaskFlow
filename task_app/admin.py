from django.contrib import admin
from .models import User, Task, Project


# Register your models here.
@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "email")
    search_fields = ("name", "email")
    list_filter = ("position",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Task)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "date", "user")
    search_fields = ("title",)
    list_filter = ("status", "date")

