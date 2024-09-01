from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import User, Task, Project


# Create your views here.
def login_site(request):
    if request.method == "POST":
        if "register" in request.POST:
            pass
        elif "login" in request.POST:
            pass
    else:
        return render(request, "login.html")


def logout_site(request):
    logout(request)
    redirect("login")


@login_required
def home(request):
    projects = Project.objects.all()
    tasks = Task.objects.all().order_by(
        "-date"
    )  # {project.name: Task.objects.filter(project=project) for project in projects}
    users = User.objects.all().order_by("name")
    return render(
        request, "home.html", {"projects": projects, "tasks": tasks, "users": users}
    )


@login_required
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


@login_required
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


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        if "concluir" in request.POST:
            task.status = "C"

        task.save()
        return redirect("home")
    return redirect("home")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")
