from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def marketing(request):
    return render(request,'digital_marketing/marketing.html')

