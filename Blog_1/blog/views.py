from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

# Create your views here.

def blog(request):

    return render(request, 'blog/blog.html')

def createPost(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        action = request.POST.get("action")  # Get draft or publish action

        # Validate the data
        if not title or len(title) < 5:
            messages.error(request, "Title must be at least 5 characters long.")
            return redirect('blog:blog')
        
        if not author or len(author) < 3:
            messages.error(request, "Author name must be at least 3 characters long.")
            return redirect('blog:blog')
            
        if not content:
            messages.error(request, "Content is required.")
            return redirect('blog:blog')
            
        if not category:
            messages.error(request, "Please select a category.")
            return redirect('blog:blog')

        try:
            # Create the post
            post = Post(
                title=title, 
                author=author, 
                content=content, 
                category=category, 
                image=image
            )
            
            # Set status based on action
            if action == "publish":
                post.status = "published"  # Assuming you have a status field
            else:
                post.status = "draft"
                
            post.save()
            
            success_message = "Your post has been published successfully." if action == "publish" else "Your post has been saved as draft."
            messages.success(request, success_message)
            
        except Exception as e:
            messages.error(request, f"An error occurred while saving the post: {str(e)}")
    
    return redirect('blog:blog')

