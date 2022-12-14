from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html", )


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if (request.POST["password1"] == request.POST["password2"]):
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("tasks")
            except IntegrityError:
                return render(request, "signup.html", {"form": UserCreationForm, "error": "El usuario ya existe"})
        else:
            return render(request, "signup.html", {"form": UserCreationForm, "error": "Las constraseñas no coinciden"})


@login_required
def tasks(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=True).order_by("-important")
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "POST":
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(request, "create_task.html", {"form": TaskForm, "error": "Ha ocurrido un error"})
    else:
        return render(request, "create_task.html", {"form": TaskForm})


@login_required
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, "task_detail.html", {"task": task, "form": form})
    else:
        try:
            task = get_object_or_404(Task, id=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(request, "task_detail.html", {"task": task, "form": form, "error": "Ingresa datos validos"})

@login_required
def complete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.datecompleted = timezone.now()
        task.save()
        print(task.datecompleted)
        return redirect("tasks")
    else:
        return redirect("editTask")

@login_required
def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        return redirect("tasks")
    else:
        return redirect("editTask")

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by("-important")
    return render(request, "completed_task.html", {"tasks": tasks})

@login_required
def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {"form": AuthenticationForm, "error": "El usuario o la contraseña son incorrectos"})
        else:
            login(request, user)
            return redirect(tasks)
