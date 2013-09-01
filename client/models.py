# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from index.models import Branch, Video


def get_display(key, list):
        d = dict(list)
        if key in d:
            return d[key]
        return None


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name=u'Ф.И.О.')
    position = models.TextField(verbose_name=u'Должность')
    characteristic = models.TextField(verbose_name=u'Характеристики')
    phone_work = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (раб.)')
    phone_cell = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (моб.)')
    address = models.TextField(blank=True, verbose_name=u'Адрес')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    icq = models.CharField(max_length=15, blank=True, verbose_name=u'ICQ')
    skype = models.CharField(max_length=50, blank=True, verbose_name=u'Skype')
    additional = models.TextField(blank=True, verbose_name=u'Дополнительные контакты')

    def __unicode__(self):
        return self.name


class Client(models.Model):
    STATUS = (
        (u'1', 'Прозвон'),
        (u'2', 'Переговоры'),
        (u'3', 'Утверждение'),
        (u'4', 'Подписан'),
        (u'5', 'Сдаюсь'),
        (u'6', 'Не наш'),
    )
    LVL = (
        (u'1', 'Менеджер'),
        (u'2', 'Администратор'),
        (u'3', 'Директор'),
        (u'4', 'Зам. директора'),
        (u'5', 'Ген. директор'),
        (u'6', 'Владелец'),
    )
    TYPE = (
        (u'1', 'Звонок'),
        (u'2', 'Повторный звонок'),
        (u'3', 'Встреча'),
        (u'4', 'Письмо'),
    )
    name_rus = models.CharField(max_length=150, verbose_name=u'Клиент (рус.)')
    name_eng = models.CharField(max_length=150, blank=True, verbose_name=u'Клиент (англ.)')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    control = models.ForeignKey(User, blank=True, limit_choices_to = {'groups__name': 'Руководители'}, verbose_name=u'На контроле')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'Статус')
    branch = models.ForeignKey(Branch, verbose_name=u'Отрасль')
    site = models.URLField(blank=True, verbose_name=u'Сайт клиента')
    notes = models.TextField(blank=True, verbose_name=u'Заметки')
    tags = models.TextField(blank=True, verbose_name=u'Тэги')
    details = models.TextField(blank=True, verbose_name=u'Юр. название, реквизиты, почтовый адрес')
    contact_lvl = models.CharField(max_length=1, choices=LVL, blank=True, verbose_name=u'Уровень контакта')
    ra = models.CharField(max_length=150, blank=True, verbose_name=u'Рекламное агенство')
    next_date = models.DateField(blank=True, verbose_name=u'Дата следующего контакта')
    contact_type = models.CharField(max_length=1, choices=TYPE, blank=True, verbose_name=u'Тип следующего контакта')
    contact_1 = models.OneToOneField(Contact, related_name='contact_1', verbose_name=u'Контакт')
    contact_2 = models.OneToOneField(Contact, related_name='contact_2', blank=True, null=True, verbose_name=u'Контакт')
    contact_3 = models.OneToOneField(Contact, related_name='contact_3', blank=True, null=True, verbose_name=u'Контакт')
    contact_result = models.TextField(verbose_name=u'Результаты контактов')
    last_date = models.DateField(blank=True, verbose_name=u'Дата последнего контакта')

    def __unicode__(self):
        return self.name_rus

    @property
    def status_verbose(self):
        return get_display(self.status, self.STATUS)

    @property
    def contact_lvl_verbose(self):
        return get_display(self.contact_lvl, self.LVL)

    @property
    def contact_type_verbose(self):
        return get_display(self.contact_type, self.TYPE)


class AdvertisingCampaign(models.Model):
    TYPE_PAYMENT = (
        (u'1', 'Деньги б/н'),
        (u'2', 'Деньги нал'),
        (u'3', 'Бартер'),
        (u'4', 'Соц. ролик'),
    )
    client = models.ForeignKey(Client, verbose_name=u'Название клиента')
    subject = models.CharField(max_length=250, verbose_name=u'Название сюжета')
    start_date = models.DateField(verbose_name=u'Старт РК')
    end_date = models.DateField(verbose_name=u'Окончание РК')
    days = models.IntegerField(verbose_name=u'Количество дней')
    video = models.ForeignKey(Video, verbose_name=u'Ролик')
    type_payment = models.CharField(max_length=1, choices=TYPE_PAYMENT, verbose_name=u'Вид оплаты')
    discount = models.CharField(max_length=100, verbose_name=u'Скидка')
    amount_paid = models.FloatField(verbose_name=u'Сумма к оплате')
    pay_date = models.DateField(verbose_name=u'Дата проплаты')
    restaurant = models.ManyToManyField(Restaurant)

    def __unicode__(self):
        return self.client.name_rus

    @property
    def type_payment_verbose(self):
        return get_display(self.type_payment, self.TYPE_PAYMENT)
