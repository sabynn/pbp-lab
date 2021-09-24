from django.db import models

# Create your models here.
class Note(models.Model):
    note_to = models.CharField(max_length=30)
    note_from = models.CharField(max_length=30)
    note_title = models.CharField(max_length=30)
    note_message = models.TextField()