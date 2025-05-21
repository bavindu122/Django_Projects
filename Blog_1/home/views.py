from django.shortcuts import render,HttpResponse
from .models import Contact


def home(request):

    return render(request, 'home/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        content = request.POST.get("content")

        # Save the data to the database
        contact = Contact(name=name, phone=phone, email=email, content=content)
        contact.save()

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

# Create your views here.
