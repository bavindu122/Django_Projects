from django.shortcuts import render,HttpResponse
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.core.paginator import Paginator



def home(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    featured_post = posts.first() if posts.exists() else None
    latest_posts = posts.exclude(id=featured_post.id) if featured_post else posts
    
    # Pagination
    paginator = Paginator(latest_posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'featured_post': featured_post,
    }
    
    return render(request, 'home/home.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        content = request.POST.get("content")
        # Validate the data
        if(len(name)<3):
            messages.error(request, "Please fill the form correctly.")
            return render(request, 'home/contact.html')
        if(len(email)<5 or email.split('@')[1] != "gmail.com"):
            messages.error(request, "Please fill the form correctly.")
            return render(request, 'home/contact.html')
        if(len(phone)<10):
            messages.error(request, "Please fill the form correctly.")
            return render(request, 'home/contact.html')
        # Save the data to the database
        contact = Contact(name=name, phone=phone, email=email, content=content)
        contact.save()
        messages.success(request, "Your message has been sent successfully.")
        

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

# Create your views here.
