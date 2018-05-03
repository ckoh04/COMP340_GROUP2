from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import json

class HomePageView(APIView):

    @csrf_exempt
    def create_or_retrieve(self, request=None, uId="test", format=None):
        if request.method == 'GET':
            try:
                found_user = Subscribe.objects.get(id=uId)
                data = { "id": found_user.id, "subLevel": found_user.subLevel}
                return HttpResponse(json.dumps(data), status=200)

            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

        if request.method == "POST":
            try:
                found_user = Subscribe.objects.get(uId=subLevel)
                #sub level
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            u = id(uId=0)
            u.save()
            return HttpResponse(json.dumps({"status":"Success"}))


