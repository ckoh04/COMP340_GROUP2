from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from score.models import Score
from user.models import User
from django.views.decorators.csrf import csrf_exempt

import json




class HomePageView(APIView):

    @csrf_exempt
    def set_or_retrieve(self, request=None, uid="0", format=None):
        if request.method == 'GET':

            try:
                found_id = Score.objects.get(userid=uid)
                data = { "id": found_id.userid, "score": found_id.value }
                return HttpResponse(json.dumps(data), status=200)

            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchId"}), status=404)

        if request.method == "POST":
            try:
                found_id = User.objects.get(id=uid)
                u = Score(value=0, userid=found_id.id)
                u.save()
                return HttpResponse(json.dumps({"status": "Success"}))
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status": "NoExistingId"}), status=403)
