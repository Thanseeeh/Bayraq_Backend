# Client Views
from rest_framework.views import APIView
from django.shortcuts import render


# HomePage
class Home(APIView):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)


# CategoriesPage
class Categories(APIView):
    def get(self, request):
        context = {}
        return render(request, 'categories.html', context)
    

# AboutUsPage
class AboutUs(APIView):
    def get(self, reqeust):
        context = {}
        return render(reqeust, 'about_us.html', context)
    

# ContactPage
class Contact(APIView):
    def get(self, reqeust):
        context = {}
        return render(reqeust, 'contact.html', context)