# Owner Views
from rest_framework.views import APIView
from rest_framework.response import Response

class NewClass(APIView):
    def get(self, request):
        return Response({"message": "this is the owner's page"})