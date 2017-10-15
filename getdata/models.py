from django.db import models


class Notes(models.Model):
    contents = models.CharField(max_length=1024)
    notetype = models.IntegerField()
