from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def contacts(request,letter = ""):
    if letter == "":
        contacts = Contact.objects.filter(user=request.user).order_by("-favorite")
        return render(request, "contacts.html", {'contacts': contacts})
        
    if letter == "Familia":
        contacts = Contact.objects.all().filter(group__exact=1,user=request.user).order_by("-favorite")
        if len(contacts) >= 1:
            return render(request, "contacts.html", {'contacts': contacts,})
        else:
            return render(request, "contacts.html", {'contacts': contacts,"error":"No tienes contactos que en ese grupo"})
    elif letter == "Amigos":
        contacts = Contact.objects.all().filter(group__exact=2,user=request.user).order_by("-favorite")
        if len(contacts) >= 1:
            return render(request, "contacts.html", {'contacts': contacts,})
        else:
            return render(request, "contacts.html", {'contacts': contacts,"error":"No tienes contactos que en ese grupo"})
    elif letter == "Trabajo":
        contacts = Contact.objects.all().filter(group__exact=3,user=request.user).order_by("-favorite")
        if len(contacts) >= 1:
            return render(request, "contacts.html", {'contacts': contacts,})
        else:
            return render(request, "contacts.html", {'contacts': contacts,"error":"No tienes contactos que en ese grupo"})
    elif letter == "Otros":
        contacts = Contact.objects.all().filter(group__exact=4,user=request.user).order_by("-favorite")
        if len(contacts) >= 1:
            return render(request, "contacts.html", {'contacts': contacts,})
        else:
            return render(request, "contacts.html", {'contacts': contacts,"error":"No tienes contactos que en ese grupo"})
    else:
        if  letter != "Familia" and letter != "Amigos" and letter != "Trabajo" and letter != "Otros" :
            contacts = Contact.objects.all().filter(name__startswith=letter,user=request.user).order_by("-favorite")
            if len(contacts) < 1:
                return render(request, "contacts.html", {'contacts': contacts,"error":"No tienes contactos que inicien con esa letra"})
            else:
                return render(request, "contacts.html", {'contacts': contacts,})
            
    
@login_required
def edit_contact(request,contact_id):
    contact = Contact.objects.get(id=contact_id,user=request.user)
    if request.method == "GET":
        form = ContactForm(instance=contact)
        return render(request, "edit_contact.html", {'contacts': contacts,"contact_id":contact_id,"form":form})
    else:
        contact_a = ContactForm(request.POST,instance=contact, )
        contact_actu = contact_a.save(commit=False)
        contact_actu.user = request.user
        contact_actu.save()
        return redirect("contacts")
    
    
@login_required
def create_contact(request):
    if request.method == "GET":
        return render(request, "create_contact.html", {"form": ContactForm})
    else:
        try:
            contact = ContactForm(request.POST)
            new_contact = contact.save(commit=False)
            new_contact.user = request.user
            new_contact.save()
            return redirect("contacts")
        except:
            return render(request, "create_contact.html", {"form": ContactForm, "error": "Ingresa datos validos"})
    
@login_required
def delete_contact(request,contact_id):
    contact = Contact.objects.get(id=contact_id,user=request.user)
    contact.delete()
    return redirect("contacts")

# Create your views here.

