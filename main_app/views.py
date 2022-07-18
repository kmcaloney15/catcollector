from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# -------- CLASS -----------------

# Add the Cat class & list and view function below the imports
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]




#  -------- DEFINE VIEWS -----------------

# Define the home view
def home(request): #request is like .req in express 
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') # this is like res.send in express

def about(request):
    return render(request, 'about.html') # render looks for templates

# Add new view
def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats}) #creating dictionary / object - cats are equal to cats