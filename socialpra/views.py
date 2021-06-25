from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def socila_pramotion(request):
    return render(request,'socialpra/social_promotion.html')

