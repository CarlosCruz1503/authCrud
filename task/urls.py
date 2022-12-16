from django.urls import path
from . import views
urlpatterns = [
    path("tasks/", views.tasks,name="tasks"),
    path("tasks/create", views.create_task,name="create_task"),
    path("tasks/delete/<int:task_id>", views.delete_task,name="delete_task"),
    path("tasks/completed/", views.completed_task,name="completed_task"),
    path("tasks/edit/<int:task_id>", views.edit_task,name="edit_task"),
    path("tasks/complete/<int:task_id>", views.complete_task,name="complete_task"),
    path("login/", views.signin, name="login"),
    path("signup/", views.signup,name="signUp"),
    path("logout/", views.signout,name="logout"),
    path("", views.home,name="home"),
    path("home/", views.home2,name="home2"),
]
