from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Show(models.Model):
    show_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Rating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    rating_text = models.CharField(max_length=200)
    rate = models.IntegerField(default=0)
