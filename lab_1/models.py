from django.db import models

# TODO Create Friend model that contains name, npm, and DOB (date of birth) here


class Friend(models.Model):
    name = models.CharField(max_length=30)
    # TODO Implement missing attributes in Friend model
