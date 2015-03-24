from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=40)
    userid = models.ForeignKey(User)
    workdate = models.DateField()
    description = models.CharField(max_length=300, blank=True)
    def __unicode__(self):
        return self.name

class StdEvent(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300, blank=True)
    def __unicode__(self):
        return self.name
