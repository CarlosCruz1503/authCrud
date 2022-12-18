from django.urls import path
from . import views
urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("contacts/<str:letter>", views.contacts, name="contacts"),
    path("contacts/edit/<int:contact_id>", views.edit_contact, name="edit_contact"),
    path("contacts/create/", views.create_contact, name="create_contact"),
    path("contacts/delete/<str:contact_id>", views.delete_contact, name="delete_contact"),
]
