from django.http import HttpResponse
from rest_framework.views import APIView
import json

class HomePageView(APIView):
    def get(self, request=None, uname="test", format=None):
        data = { "user": uname, "key2": "value2" }
        return HttpResponse(json.dumps(data))