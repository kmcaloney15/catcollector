from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView
from .models import Cat
from django.http import HttpResponse
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm



#  -------- DEFINE VIEWS -----------------

# Define the home view


def home(request):  # request is like .req in express
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') # this is like res.send in express
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')  # render looks for templates


# Add new view
def cats_index(request):
  cats = Cat.objects.all()
  # creating dictionary / object - cats are equal to cats
  return render(request, 'cats/index.html', {'cats': cats})


def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})


class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'


class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'
