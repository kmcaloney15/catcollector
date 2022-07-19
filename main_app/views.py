from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from models import Cat

#  -------- DEFINE VIEWS -----------------

# Define the home view
def home(request): #request is like .req in express 
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') # this is like res.send in express

def about(request):
    return render(request, 'about.html') # render looks for templates

# Add new view
def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats }) #creating dictionary / object - cats are equal to cats