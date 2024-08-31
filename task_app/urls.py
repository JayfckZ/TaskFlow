from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/create_project/", views.create_project, name="create_project"),
    path("home/<int:project_id>/add_task/", views.add_task, name="add_task"),
    path("home/delete_task/<int:task_id>", views.delete_task, name="delete_task"),
]
