# Owner Views
from rest_framework.views import APIView
from django.shortcuts import render
    
# AdminHomePage
class AdminHome(APIView):
    def get(self, request):
        context = {}
        return render(request, 'admin_home.html', context)