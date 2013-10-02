# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from index.models import Video


YN = (
    (u'0', 'Нет'),
    (u'1', 'Да'),
)

def get_display(key, list):
        d = dict(list)
        if key in d:
            return d[key]
        return None


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __unicode__(self):
        return self.name


class AdvertisingAgency(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название')

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
    name = models.CharField(max_length=200, verbose_name=u'Клиент')
    adv_ag = models.ForeignKey(AdvertisingAgency, blank=True, null=True, verbose_name=u'Рекламное агентство')
    payer = models.CharField(max_length=200, blank=True, verbose_name=u'Плательщик')
    brand = models.CharField(max_length=200, blank=True, verbose_name=u'Бренд')
    branch = models.ForeignKey(Branch, blank=True, null=True, verbose_name=u'Отрасль')
    site = models.URLField(blank=True, verbose_name=u'Сайт')
    notes = models.TextField(blank=True, verbose_name=u'Примечания')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'Статус')
    payer_vat = models.CharField(max_length=1, choices=YN, verbose_name=u'Плательщик НДС')
    payer_cert = models.FileField(upload_to=u'payer_cert', blank=True, verbose_name=u'Свидетельство плательщика')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    negot_res = models.TextField(blank=True, verbose_name=u'Результаты переговоров')
    last_cont_date = models.DateField(blank=True, null=True, verbose_name=u'Дата последнего контакта')
    contact_plan = models.TextField(blank=True, verbose_name=u'План следующего контакта')
    next_cont_date = models.DateField(blank=True, null=True, verbose_name=u'Дата следующего контакта')
    username = models.ForeignKey(User, blank=True)

    def __unicode__(self):
        return self.name

    @property
    def status_verbose(self):
        return get_display(self.status, self.STATUS)

    @property
    def payer_vat_verbose(self):
        return get_display(self.payer_vat, YN)


class Contact(models.Model):
    POSITION = (
        (u'1', 'Менеджер'),
        (u'2', 'Администратор'),
        (u'3', 'Директор'),
        (u'4', 'Зам. директора'),
        (u'5', 'Ген. директор'),
        (u'6', 'Владелец'),
    )
    client = models.ForeignKey(Client, verbose_name=u'Клиент', related_name='contact')
    name = models.CharField(max_length=200, verbose_name=u'Ф.И.О.')
    position = models.TextField(verbose_name=u'Должность')
    phone_work = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (раб.)')
    phone_cell = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (моб.)')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    icq = models.CharField(max_length=25, blank=True, verbose_name=u'ICQ')
    skype = models.CharField(max_length=100, blank=True, verbose_name=u'Skype')
    address = models.TextField(blank=True, verbose_name=u'Фактический адрес')
    additional = models.TextField(blank=True, verbose_name=u'Дополнительные контакты')

    def __unicode__(self):
        return self.name

    @property
    def position_verbose(self):
        return get_display(self.position, self.POSITION)


class AdvertisingCampaign(models.Model):
    TYPE_PAYMENT = (
        (u'1', 'Деньги б/н'),
        (u'2', 'Деньги нал'),
        (u'3', 'Бартер'),
        (u'4', 'Соц. ролик'),
    )
    client = models.ForeignKey(Client, verbose_name=u'Название клиента', related_name='ac')
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


class Details(models.Model):
    client = models.OneToOneField(Client, verbose_name=u'Название клиента', related_name='details')
    legal_name = models.CharField(max_length=200, verbose_name=u'Юридическое название')
    code = models.IntegerField()
    index = models.IntegerField(blank=True, verbose_name=u'Индекс')
    region = models.CharField(max_length=200, blank=True, verbose_name=u'Область')
    city = models.CharField(max_length=200, blank=True, verbose_name=u'Город')
    street = models.CharField(max_length=200, blank=True, verbose_name=u'Улица')
    house1 = models.CharField(max_length=20, blank=True, verbose_name=u'Дом')
    house2 = models.CharField(max_length=20, blank=True, verbose_name=u'Корпус')
    room1 = models.CharField(max_length=20, blank=True, verbose_name=u'Квартира')
    office = models.CharField(max_length=20, blank=True, verbose_name=u'Офис')
    room2 = models.CharField(max_length=20, blank=True, verbose_name=u'Комната')
    phone = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона')
    bank = models.CharField(max_length=150, blank=True, verbose_name=u'Название банка')
    mfo = models.IntegerField(max_length=6, blank=True, verbose_name=u'МФО')
    current_account = models.IntegerField(max_length=14, blank=True, verbose_name=u'Расчетный счет')
    vat_inn = models.IntegerField(max_length=12, blank=True)
