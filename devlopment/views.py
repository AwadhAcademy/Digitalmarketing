from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def devlopment(request):
    return render(request,'devlopment/devlopment.html')

