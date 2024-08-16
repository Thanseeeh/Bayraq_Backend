# Owner Urls
from django.urls import path
from .views import AdminHome

urlpatterns = [
    path('', AdminHome.as_view(), name="admin"),
]
