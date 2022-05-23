from django.shortcuts import render
from .forms import ContactForm
from .models import Contact, AboutUsModel, HomeSlider, Gallery, Stuff
from foods.models import FoodMenu


def homeViews(request):
    slider_header = HomeSlider.objects.all()
    aboutus_home = AboutUsModel.objects.last()
    foods = FoodMenu.objects.filter(status=True)
    gallery = Gallery.objects.all()
    context = {
        'slider_header': slider_header,
        'aboutus_home': aboutus_home,
        'foods': foods,
        'gallery': gallery,
    }
    return render(request, 'core/home.html', context)

def contactUsView(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            Contact.objects.create(name=name, email=email, subject=subject, body=body)
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', context={'form': form})


def aboutUsView(request):
    about = AboutUsModel.objects.last()
    foods = FoodMenu.objects.filter(status=True)
    context = {
        'about': about,
        'foods': foods,
    }
    return render(request, 'core/about.html', context)


def StuffView(request):
    stuff = Stuff.objects.all()

    return render(request, 'core/stuff.html', context={'stuff': stuff})
