from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Cat

#  -------- DEFINE VIEWS -----------------

# Define the home view
def home(request): #request is like .req in express 
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') # this is like res.send in express
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') # render looks for templates

# Add new view
def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats }) #creating dictionary / object - cats are equal to cats


def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })


# def CatCreate(request, cat_id):
#     cat = Cat.objects.get(id=cat_id)
#     return HttpResponse(f"Filler cat create page")
    # return render(request, 'cats/create.html', { 'cat': cat })