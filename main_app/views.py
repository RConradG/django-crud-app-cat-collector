from django.shortcuts import render
from django.http import HttpResponse

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