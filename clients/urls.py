# Client Urls
from django.urls import path
from .views import HelloWorldAPIView

urlpatterns = [
    path('api/helloworld', HelloWorldAPIView.as_view(), name="hello world"),
]
