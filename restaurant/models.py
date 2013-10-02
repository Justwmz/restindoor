# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from index.models import Video


def get_display(key, list):
        d = dict(list)
        if key in d:
            return d[key]
        return None


class Restriction(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Restaurant(models.Model):
    CITY = (
        (u'1', 'Киев'),
        (u'2', 'Киевская обл.'),
    )
    FORM_COOP = (
        (u'1', 'Стандарт'),
        (u'2', 'Баинг'),
    )
    STATUS = (
        (u'1', 'Стандарт'),
        (u'2', 'Бизнес'),
        (u'3', 'Козырная карта'),
        (u'4', 'Премиум'),
    )
    PAYMENT_TERM = (
        (u'1', '100% предоплаты'),
        (u'2', '50%/50% в поточном месяце'),
        (u'3', 'Оплата постфактум'),
    )
    ORG_FORM = (
        (u'1', 'ООО'),
        (u'2', 'ФОП'),
    )
    WARRANTY_MAIL = (
        (u'1', 'Не требуется'),
        (u'2', 'Подписано'),
        (u'3', 'Не подписано'),
    )
    BROADCAST = (
        (u'1', 'Система ресторана'),
        (u'2', 'Система RESTindoor'),
        (u'3', 'Баинг'),
    )
    logo = models.ImageField(upload_to='logo', blank=True, verbose_name=u'Логотип')
    name_rus = models.CharField(max_length=150, verbose_name=u'Ресторан (рус.)')
    name_eng = models.CharField(max_length=150, blank=True, verbose_name=u'Ресторан (англ.)')
    chain_name_rus = models.CharField(max_length=150, blank=True, verbose_name=u'Сеть ресторанов (рус.)')
    chain_name_eng = models.CharField(max_length=150, blank=True, verbose_name=u'Сеть ресторанов (англ.)')
    rest_open = models.TimeField(verbose_name=u'Начало работы ресторана')
    rest_close = models.TimeField(verbose_name=u'Конец работы ресторана')
    broadcast = models.CharField(max_length=1, choices=BROADCAST, verbose_name=u'Система вещания')
    site = models.URLField(blank=True, verbose_name=u'Сайт ресторана')
    city = models.CharField(max_length=1, choices=CITY, verbose_name=u'Город/Область')
    address = models.TextField(blank=True, verbose_name=u'Адрес')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    form_coop = models.CharField(max_length=1, choices=FORM_COOP, verbose_name=u'Форма сотрудничества')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'Статус')
    sum_payment = models.FloatField(verbose_name=u'Сумма оплаты с НДС')
    sum_payment_min = models.FloatField(verbose_name=u'Грн. за мин.')
    payment_term = models.CharField(max_length=1, choices=PAYMENT_TERM, verbose_name=u'Условия оплаты')
    pay_term_com = models.TextField(blank=True, verbose_name=u'Комментарии к оплате')
    org_form = models.CharField(max_length=1, choices=ORG_FORM, verbose_name=u'Организационная форма')
    stat_doc_1 = models.BooleanField()
    stat_doc_2 = models.BooleanField()
    stat_doc_3 = models.BooleanField()
    stat_doc_4 = models.BooleanField()
    contract = models.BooleanField(verbose_name=u'Договор')
    act_rec_trans = models.BooleanField(verbose_name=u'Акт приема передачи')
    warranty_mail = models.CharField(max_length=1, choices=WARRANTY_MAIL, verbose_name=u'Гарантийное письмо на изображение физ. лица')
    list_restrict = models.BooleanField(verbose_name=u'Список ограничений')
    restriction = models.ManyToManyField(Restriction, blank=True, verbose_name=u'Ограничения')
    equipment = models.BooleanField(verbose_name=u'Оборудование')
    plasma_work = models.IntegerField(blank=True, default=0, verbose_name=u'Количество подключенных плазм')
    plasma_all = models.IntegerField(blank=True, default=0, verbose_name=u'Общее количество плазм')
    username = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

#    class Meta:
#        permissions = (
#            ('view_name_rus', 'Название на русском'),
#            ('view_name_eng', 'Название на английском'),
#            ('view_form_coop', 'Форма сотрудничества'),
#            ('view_chain_name_rus', 'Название сети на русском'),
#            ('view_chain_name_eng', 'Название сети на английском'),
#            ('view_city', 'Город'),
#            ('view_add_date', 'Дата создания'),
#            ('view_status', 'Статус'),
#            ('view_site', 'Сайт'),
#            ('view_org_form', 'Организационная форма'),
#            ('view_details', 'Реквизиты'),
#            ('view_contact', 'Контакт'),
#            ('view_payment_term', 'Условия оплаты'),
#            ('view_sum_payment', 'Сумма оплаты'),
#            ('view_chain_avail', 'Наличие своей сети'),
#            ('view_equipment', 'Оборудование'),
#            ('view_plasma_all', 'Общее количество плазм'),
#            ('view_plasma_work', 'Количество подключенных плазм'),
#            ('view_contract', 'Договор'),
#            ('view_act_rec_trans', 'Акт приема передачи'),
#            ('view_list_restrict', 'Список ограничений'),
#            ('view_restriction', 'Ограничения'),
#            ('view_video', 'Ролик'),
#            ('view_warranty_mail', 'Гарантийное письмо на изображение физ. лица'),
#            ('view_stat_doc_1', 'stat_doc_1'),
#            ('view_stat_doc_2', 'stat_doc_2'),
#            ('view_stat_doc_3', 'stat_doc_3'),
#            ('view_stat_doc_4', 'stat_doc_4'),
#        )

    def __unicode__(self):
        return self.name_rus

    @property
    def form_coop_verbose(self):
        return get_display(self.form_coop, self.FORM_COOP)

    @property
    def city_verbose(self):
        return get_display(self.city, self.CITY)

    @property
    def status_verbose(self):
        return get_display(self.status, self.STATUS)

    @property
    def org_form_verbose(self):
        return get_display(self.org_form, self.ORG_FORM)

    @property
    def payment_term_verbose(self):
        return get_display(self.payment_term, self.PAYMENT_TERM)

    @property
    def warranty_mail_verbose(self):
        return get_display(self.warranty_mail, self.WARRANTY_MAIL)

    @property
    def broadcast_verbose(self):
        return get_display(self.broadcast, self.BROADCAST)


class Contact(models.Model):
    POSITION = (
        (u'1', 'Владелец'),
        (u'2', 'Директор'),
        (u'3', 'Менеджер'),
        (u'4', 'Администратор'),
        (u'5', 'Бухгалтер'),
        (u'6', 'Тех. отдел'),
    )
    restaurant = models.ForeignKey(Restaurant, verbose_name=u'Ресторан', related_name='contact')
    name = models.CharField(max_length=150, verbose_name=u'Ф.И.О.')
    position = models.CharField(max_length=1, choices=POSITION, verbose_name=u'Должность')
    phone_work = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (раб.)')
    phone_cell = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (моб.)')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    icq = models.CharField(max_length=15, blank=True, verbose_name=u'ICQ')
    skype = models.CharField(max_length=50, blank=True, verbose_name=u'Skype')
    address = models.TextField(blank=True, verbose_name=u'Фактический адрес')
    additional = models.TextField(blank=True, verbose_name=u'Дополнительные контакты')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True, related_name='restaurant_contact')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    @property
    def position_verbose(self):
        return get_display(self.position, self.POSITION)


class Details(models.Model):
    restaurant = models.OneToOneField(Restaurant, verbose_name=u'Ресторан', related_name='details')
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
    add_date = models.DateField(auto_now_add=True, verbose_name=u'Дата внесения в базу')
    username = models.ForeignKey(User, null=True, blank=True, related_name='restaurant_details')
    is_active = models.BooleanField(default=True)
