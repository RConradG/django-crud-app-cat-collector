from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat
# Create your views here.
# controller code in python
# we call these views functions
def home(request):
    # each view function or "view"
    # receives a request object
    return render(request, 'home.html')
# to send a response we return it!

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })
    
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    # fields = '__all__'
    fields = ['name', 'breed', 'description', 'age']