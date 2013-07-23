# -*- coding: utf-8 -*- 
from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    periodicity = models.CharField(max_length=30, default='1 раз в час')
    moder_launch = models.BooleanField()

    def __unicode__(self):
        return self.name
