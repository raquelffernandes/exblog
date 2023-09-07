from django.shortcuts import render
from .models import Post


# Create your views her
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html',{"post": post})
