from django.db import models

class Score(models.Model):
    userid = models.IntegerField(primary_key=True)
    value = models.IntegerField(default=0)