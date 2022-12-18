from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def tasks(request):
    tasks = Task.objects.filter(
        user=request.user, date_complete__isnull=True).order_by("date_for_complete")
    categories = Category.objects.all()
    return render(request, "tasks.html", {"tasks": tasks,"categories": categories})


@login_required
def completed_task(request):
    tasks = Task.objects.filter(
        user=request.user, date_complete__isnull=False).order_by("date_for_complete")
    categories = Category.objects.all()
    return render(request, "completed_task.html", {"tasks": tasks,"categories": categories})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": TaskForm})
    else:
        try:
            task = TaskForm(request.POST)
            new_task = task.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except:
            return render(request, "create_task.html", {"form": TaskForm, "error": "Ingresa datos validos"})


@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    form = TaskForm(instance=task)
    if request.method == "GET":
        return render(request, "edit_task.html", {"form": form, "task_id": task_id})
    else:
        try:
            task_a = TaskForm(request.POST, instance=task)
            task_actu = task_a.save(commit=False)
            task_actu.user = request.user
            task_actu.save()
            return redirect("tasks")
        except:
            return render(request, "edit_task.html", {"form": form, "task_id": task_id, "error": "Ingresa datos validos"})


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect("tasks")


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.date_complete = timezone.now()
    task.save()
    return redirect("tasks")


def signup(request):
    if request.method == "GET":
        return render(request, "signUp.html", {})
    else:
        if len(request.POST["password1"]) >= 8:
            if request.POST["password1"] == request.POST["password2"]:
                try:
                    user = User.objects.create_user(
                        username=request.POST["username"], password=request.POST["password1"])
                    user.save()
                    login(request, user)
                    return redirect("home2")
                except:
                    return render(request, "signUp.html", {"error": "El usuario ya existe"})
            else:
                return render(request, "signUp.html", {"error": "La contraseñas deben ser iguales"})
        else:
            return render(request, "signUp.html", {"error": "La contraseña debe se de minimo 8 caracteres"})


def signin(request):
    if request.method == "GET":
        return render(request, "login.html", {})
    else:
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"])
        try:
            login(request, user)
            return redirect("home2")
        except:
            return render(request, "login.html", {"error": "El usuario o la contraseña son incorrectos"})


def home(request):
    name="admin123"
    password="admin123"
    try:
        user = User.objects.create_superuser(
            username=name, password=password)
        user.save()
        return render(request, "home.html", {})
    except:
        return render(request, "home.html", {})



@login_required
def signout(request):
    logout(request)
    return redirect("login")

def home2(request):
    return render(request,"home2.html",{})