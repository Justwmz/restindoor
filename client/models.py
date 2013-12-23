# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant
from index.models import Video


YN = (
    (u'0', 'Нет'),
    (u'1', 'Да'),
)

STATUS = (
    (u'1', 'Активный'),
    (u'2', 'Подписан'),
    (u'3', 'Сдаюсь'),
    (u'4', 'Не наш'),
    (u'5', 'Переговоры'),
)

def get_display(key, list):
        d = dict(list)
        if key in d:
            return d[key]
        return None


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class AdvertisingAgency(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название')
    is_client = models.BooleanField(verbose_name=u'Является клиентом')
    branch = models.ForeignKey(Branch, blank=True, null=True, verbose_name=u'Отрасль')
    site = models.URLField(blank=True, verbose_name=u'Сайт')
    notes = models.TextField(blank=True, verbose_name=u'Примечания')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'Статус')
    payer_vat = models.CharField(max_length=1, choices=YN, verbose_name=u'Плательщик НДС')
    payer_cert = models.FileField(upload_to=u'payer_cert', blank=True, verbose_name=u'Свидетельство плательщика')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Клиент')
    adv_ag = models.CharField(max_length=200, blank=True, verbose_name=u'Рекламное агентство')
    branch = models.ForeignKey(Branch, blank=True, null=True, verbose_name=u'Отрасль')
    site = models.URLField(blank=True, verbose_name=u'Сайт')
    notes = models.TextField(blank=True, verbose_name=u'Примечания')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'Статус')
    payer_vat = models.CharField(blank=True, max_length=1, choices=YN, verbose_name=u'Плательщик НДС')
    payer_cert = models.FileField(upload_to=u'payer_cert', blank=True, verbose_name=u'Свидетельство плательщика')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name

    @property
    def status_verbose(self):
        return get_display(self.status, STATUS)

    @property
    def payer_vat_verbose(self):
        return get_display(self.payer_vat, YN)


class NegotiationResult(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, verbose_name=u'Клиент', related_name='client_neg_res')
    agency = models.ForeignKey(AdvertisingAgency, null=True, blank=True, verbose_name=u'Рекламное агентство', related_name='agency_neg_res')
    negot_res = models.TextField(blank=True, verbose_name=u'Результаты переговоров')
    last_cont_date = models.DateField(blank=True, null=True, verbose_name=u'Дата последнего контакта')
    contact_plan = models.TextField(blank=True, verbose_name=u'План следующего контакта')
    next_cont_date = models.DateField(blank=True, null=True, verbose_name=u'Дата следующего контакта')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Contact(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, verbose_name=u'Клиент', related_name='client_contact')
    agency = models.ForeignKey(AdvertisingAgency, null=True, blank=True, verbose_name=u'Рекламное агентство', related_name='agency_contact')
    name = models.CharField(max_length=200, blank=True, verbose_name=u'Ф.И.О.')
    position = models.TextField(blank=True, verbose_name=u'Должность')
    phone_work = models.CharField(max_length=15, blank=True, verbose_name=u'Раб. номер')
    phone_cell = models.CharField(max_length=15, blank=True, verbose_name=u'Моб. номер')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    icq = models.CharField(max_length=25, blank=True, verbose_name=u'ICQ')
    skype = models.CharField(max_length=100, blank=True, verbose_name=u'Skype')
    address = models.TextField(blank=True, verbose_name=u'Фактический адрес')
    additional = models.TextField(blank=True, verbose_name=u'Дополнительные контакты')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True, related_name='client_contact')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Details(models.Model):
    client = models.OneToOneField(Client, null=True, blank=True, verbose_name=u'Название клиента', related_name='contact_details')
    agency = models.ForeignKey(AdvertisingAgency, null=True, blank=True, verbose_name=u'Рекламное агентство', related_name='agency_details')
    legal_name = models.CharField(max_length=200, blank=True, verbose_name=u'Юридическое название')
    code = models.CharField(max_length=10, blank=True, verbose_name=u'Код ЕДРПОУ/Идент. код')
    index = models.CharField(max_length=5, blank=True, verbose_name=u'Инд.')
    region = models.CharField(max_length=200, blank=True, verbose_name=u'Область')
    city = models.CharField(max_length=200, blank=True, verbose_name=u'Город')
    street = models.CharField(max_length=200, blank=True, verbose_name=u'Улица')
    house1 = models.CharField(max_length=20, blank=True, verbose_name=u'Дом')
    house2 = models.CharField(max_length=20, blank=True, verbose_name=u'Корпус')
    room1 = models.CharField(max_length=20, blank=True, verbose_name=u'Кв.')
    office = models.CharField(max_length=20, blank=True, verbose_name=u'Офис')
    room2 = models.CharField(max_length=20, blank=True, verbose_name=u'Комн.')
    phone = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона')
    bank = models.CharField(max_length=150, blank=True, verbose_name=u'Название банка')
    mfo = models.CharField(max_length=6, blank=True, verbose_name=u'МФО')
    current_account = models.CharField(max_length=14, blank=True, verbose_name=u'Расчетный счет')
    vat_inn = models.CharField(max_length=12, blank=True, verbose_name=u'Номер свидетельства НДС/ИНН')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True, related_name='client_details')
    is_active = models.BooleanField(default=True)


class Payer(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, related_name='client_payer')
    agency = models.ForeignKey(AdvertisingAgency, null=True, blank=True, related_name='agency_payer')
    payer = models.CharField(max_length=200, blank=True, verbose_name=u'Плательщик')

    def __unicode__(self):
        return self.payer


class Brand(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, related_name='client_brand')
    agency = models.ForeignKey(AdvertisingAgency, null=True, blank=True, related_name='agency_brand')
    brand = models.CharField(max_length=200, blank=True, verbose_name=u'Бренд')

    def __unicode__(self):
        return self.brand


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
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.client.name_rus

    @property
    def type_payment_verbose(self):
        return get_display(self.type_payment, self.TYPE_PAYMENT)
