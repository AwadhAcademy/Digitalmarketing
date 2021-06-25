from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def insta(request):
    return render(request,'insta/insta.html')

