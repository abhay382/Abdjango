from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index (request):

    return render(request,'index.html')


def factorytour (request):
    return render(request,'factorytour.html')





def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'index.html', {'thank': thank})





def about (request):
    return render(request,'about.html')




def faq (request):
    return render(request,'frequentlyaskedquestion.html')


def tour (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Tour = tour(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'factorytour.html', {'thank': thank})