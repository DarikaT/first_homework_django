from django.urls import path
from .views import HomeView, AboutUs, Contacts, GalleryView


urlpatterns = [
    path('', HomeView, name = 'home_url'),
    path('about/', AboutUs, name = 'about_url'),
    path('contacts/', Contacts, name = 'contacts_url'),
    path('gallery/', GalleryView.as_view(), name = 'gallery_url'),
    
]