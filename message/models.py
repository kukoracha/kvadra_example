from django.db import models
from django.utils import timezone

class Message(models.Model):
    txt = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'message'
    def __str__(self):
        return self.txt

# Create your models here.
