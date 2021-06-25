from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def youtube(request):
    return render(request,'youtube/youtube.html')

