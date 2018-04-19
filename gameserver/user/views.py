from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import json

class HomePageView(APIView):
	@csrf_exempt
	
	def create_or_retrieve(self, request = None, uname ="test", format=None):

		if request.method == "POST":
			try: 
				found_user = user.objects.get(name=uname)
				return HttpResponse(json.dumps({"status": "AlreadyExists"}), status = 403)
			except ObjectDoesNotExist as e: 
				pass 

			u = User(name =uname)
			u.save()
			return HttpResponse(json.dumps("status":"Success"))


    
   # def get(self, request=None, uname="test", format=None):
   #     data = { "user": uname, "key2": "value2" }
   #     return HttpResponse(json.dumps(data))