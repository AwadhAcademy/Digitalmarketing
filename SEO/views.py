from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def SEO(request):
    return render(request,'SEO/SEO.html')

