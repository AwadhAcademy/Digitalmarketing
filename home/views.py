from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def front(request):
    return render(request,'home/home.html')

