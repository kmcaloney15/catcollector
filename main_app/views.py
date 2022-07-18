from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request): #request is like .req in express 
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') # this is like res.send in express

def about(request):
    return render(request, 'about.html')