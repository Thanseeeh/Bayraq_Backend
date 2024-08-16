# Client Views
from rest_framework.views import APIView
from django.shortcuts import render

# HomePage
class Home(APIView):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)