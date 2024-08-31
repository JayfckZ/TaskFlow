from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Task, Project


# Create your views here.
def home(request):
    projects = Project.objects.all()
    tasks = Task.objects.all().order_by(
        "-date"
    )  # {project.name: Task.objects.filter(project=project) for project in projects}
    users = User.objects.all().order_by("name")
    return render(
        request, "home.html", {"projects": projects, "tasks": tasks, "users": users}
    )


def create_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            try:
                Project.objects.create(name=name)
                return redirect("home")
            except:
                return redirect("home")
    return render(request, "home.html")


def add_task(request, project_id):
    if request.method == "POST":
        project = Project.objects.get(id=project_id)
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            status="P",
            user=request.user,
            project=project,
        )
    return redirect("home")


def delete_task(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")
