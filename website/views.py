from django.http import HttpResponse,JsonResponse , HttpResponseRedirect
from django.shortcuts import render
from website.forms import contactForm , NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance.name = 'unknown'
            instance.save()
            messages.add_message(request,messages.SUCCESS , 'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR , 'your ticket didnt submitted')
            

    form = contactForm() 
    return render(request,'website/contact.html' , {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponseRedirect('/')
    else:
        print('not valid')
        return HttpResponseRedirect('/')
            
        

