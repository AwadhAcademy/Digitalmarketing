from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def about_us(request):
    return render(request,'about_us/about_us.html')

