from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_site, name="login_site"),
    path("logout/", views.logout_site, name="logout_site"),
    path("home/", views.home, name="home"),
    path("home/create_project/", views.create_project, name="create_project"),
    path("home/<int:project_id>/add_task/", views.add_task, name="add_task"),
    path("home/delete_task/<int:task_id>", views.delete_task, name="delete_task"),
    path("home/update_task/<int:task_id>", views.update_task, name="update_task"),
    path(
        "home/update_project/<int:project_id>",
        views.update_project,
        name="update_project",
    ),
    path(
        "home/delete_project/<int:project_id>",
        views.delete_project,
        name="delete_project",
    ),
]
