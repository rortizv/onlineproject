from django.shortcuts import render
from blog.models import Post


def posts(request):
    # Get all posts from the database
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})
