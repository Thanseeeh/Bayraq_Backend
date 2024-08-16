# Owner Urls
from django.urls import path
from .views import NewClass

urlpatterns = [
    path('api/newclass', NewClass.as_view(), name="newclass"),
]
