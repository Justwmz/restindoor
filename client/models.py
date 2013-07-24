# -*- coding: utf-8 -*- 
from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __unicode__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    address = models.CharField(max_length=200, verbose_name=u'Адрес на сервере')
    start_date = models.DateField(verbose_name=u'Дата начала ролика')
    end_date = models.DateField(verbose_name=u'Дата окончания ролика')
    periodicity = models.CharField(max_length=30, default='1 раз в час', verbose_name=u'Периодичность ролика')
    moder_launch = models.BooleanField(verbose_name=u'Запуск модератором ролика')

    def __unicode__(self):
        return self.name
