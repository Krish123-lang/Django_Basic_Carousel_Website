from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.



def home(request):
    context = {
        "a": "apple"
    }
    return render(request, "home.html", context)


def about(request):
    context = {
        "a": "about"
    }
    return render(request, "about.html", context)


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = Contact(fullname=fullname, email=email, desc=desc)
        contact.save()

        messages.success(request, "Message Sent Successfully !!!")
        return redirect('home')
    return render(request, "contact.html")