from multiprocessing import context
from django.shortcuts import render
from .models import Post

def home(request):
     posts = Post.objects.all()
     malumotlar = {
          'posts': posts
     }
     return render (request, "index.html", context=malumotlar)
def example(request):
     posts = Post.objects.all()
     malumotlar = {
          'posts': posts
     }
     return render(request, "exsamp.html", context=malumotlar)