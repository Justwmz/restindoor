# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant


class Contact(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name=u'Ресторан', related_name='contact_tech')
    name = models.CharField(max_length=200, verbose_name=u'Ф.И.О.')
    position = models.TextField(verbose_name=u'Должность')
    phone_work = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (раб.)')
    phone_cell = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (моб.)')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    icq = models.CharField(max_length=25, blank=True, verbose_name=u'ICQ')
    skype = models.CharField(max_length=100, blank=True, verbose_name=u'Skype')
    address = models.TextField(blank=True, verbose_name=u'Фактический адрес')
    additional = models.TextField(blank=True, verbose_name=u'Дополнительные контакты')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True, related_name='tech_contact')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Device(models.Model):
    restaurant = models.OneToOneField(Restaurant, verbose_name=u'Ресторан', related_name='device')
    survey = models.BooleanField(blank=True, verbose_name=u'Обследование')
    survey_date = models.DateField(blank=True, null=True, verbose_name=u'Дата обследования')
    installation = models.BooleanField(blank=True, verbose_name=u'Монтаж')
    installation_date = models.DateField(blank=True, null=True, verbose_name=u'Дата монтажа')
    problems = models.TextField(blank=True, verbose_name=u'Проблематика')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


