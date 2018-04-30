from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from score.models import Score
from user.models import User
from django.views.decorators.csrf import csrf_exempt

import json




class HomePageView(APIView):

    @csrf_exempt
    def set_or_retrieve(self, request=None, uname="test", uscore="0", format=None):
        if request.method == 'GET':

            try:

                found_user = User.objects.get(name=uname)
                found_score = Score.objects.get(userid=found_user.id)
                data = { "id": found_user.id, "score": found_score.value }
                return HttpResponse(json.dumps(data), status=200)
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoExistingUser"}), status=404)

        if request.method == "POST":
            try:
                found_user = User.objects.get(name=uname)
                if Score.objects.get(userid=found_user.id):
                    return HttpResponse(json.dumps({"status": "UserAlreadyExists"}), status=403)
                u = Score(value=uscore, userid=found_user.id)
                u.save()
                return HttpResponse(json.dumps({"status": "Success"}))
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status": "NoExistingUser"}), status=403)

        if request.method == "PUT":
            try:
                found_user = User.objects.get(name=uname)
                u = Score(value=uscore, userid=found_user.id)
                u.save()
                return HttpResponse(json.dumps({"status": "Success"}))
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status": "NoExistingUser"}), status=403)