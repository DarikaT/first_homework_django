from django.shortcuts import render
from django.views.generic import ListView
from .models import Images

def HomeView(request):
    return render(request, 'app/home.html')

def AboutUs(request):
        data = ''
        with open('about.txt', 'w') as file:
            y = file.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum')

        with open('about.txt') as new_file:
            data = new_file.read()
        readfile = data

        return render(request, 'app/about.html', {'readfile':readfile})

def Contacts(request):
    with open('contacts.txt', 'w') as file:
        y = file.write('Someone:' '0778675767' ' Another:' '0555676767'
        ' Wow:' '0555345588' ' FuckedUp:'  '0228888893')
       
    with open('contacts.txt') as new_file:
        data = new_file.read().split()
    

    read_contacts = data

    return render(request, 'app/contacts.html', {'read_contacts':read_contacts})

class GalleryView(ListView):
    template_name = 'app/gallery.html'
    model = Images
