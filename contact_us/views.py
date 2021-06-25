from django.shortcuts import render
from django.http import HttpResponse
# from .models import contact
from .models import contact
# Create your views here.

#front Python part()
def contact_us(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        site=request.POST.get('site')
        address=request.POST.get('address')
        text=request.POST.get('text')
        phone=request.POST.get('phone')

        # contact.name=name
        # contact.email=email
        # contact.site=site
        # contact.address=address
        # contact.text=text
        # contact.phone=phone
        # contact.save()
        data=contact(name=name,email=email,site=site,address=address,text=text,phone=phone)
        data.save()


    return render(request,'contact_us/contact_us.html')


