from django.db import models


class Friend(models.Model):
    name = models.CharField(max_length=30)
    npm = models.BigIntegerField()
    dob = models.DateField(max_length=8)
