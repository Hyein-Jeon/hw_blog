from django.shortcuts import render, get_object_or_404
from .models import Blogapp

# Create your views here.

def house(request):
    blogss = Blogapp.objects.all()
    return render(request, 'house.html', {'blogss':blogss})

def more(request, blog_id):
    blog_1 = get_object_or_404(Blogapp, pk = blog_id)
    return render(request, 'more.html', {'blog_1':blog_1})
