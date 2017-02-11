from __future__ import unicode_literals

from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=200)
    intro = models.TextField()
    pdis = models.TextField()
    rating = models.FloatField()
    def __str__(self):
        return self.name

class Counter(models.Model):
    name = models.CharField(max_length=200)
    intro = models.TextField()
    usage = models.TextField()
    contact_details = models.TextField()
    def __str__(self):
        return self.name