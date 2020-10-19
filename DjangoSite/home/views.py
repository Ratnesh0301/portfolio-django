from django.shortcuts import render, HttpResponse
from home.models import Contact


# Create your views here.
def index(request):
    context = {'name': "Ratnesh", 'domain': 'Machine Learning'}
    return render(request, 'home.html', context)


def project(request):
    # return HttpResponse("This is my projects page")
    return render(request, 'project.html')


def about(request):
    # return HttpResponse("This is my about page")
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
        print("The data is saved to db.")

    # return HttpResponse("This is my contact page")
    return render(request, 'contact.html')
