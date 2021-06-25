from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def facebook(request):
    return render(request,'facebook/facebook.html')