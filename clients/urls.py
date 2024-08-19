# Client Urls
from django.urls import path
from .views import Home, Categories, AboutUs, Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('categories/', Categories.as_view(), name='categories'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),
    path('contact', Contact.as_view(), name='contact'),
]
