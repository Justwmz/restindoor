# -*- coding: utf-8 -*- 
from django.db import models
from client.models import Branch, Video


def get_display(key, list):
        d = dict(list)
        if key in d:
            return d[key]
        return None


class Contact(models.Model):
    LVL = (
        (u'в', 'Владелец'),
        (u'д', 'Директор'),
        (u'а', 'Администратор'),
        (u'м', 'Менеджер'),
    )
    name = models.CharField(max_length=150, verbose_name=u'Ф.И.О.')
    lvl = models.CharField(max_length=1, choices=LVL, verbose_name=u'Уровень контакта')
    phone_work = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (раб.)')
    phone_cell = models.CharField(max_length=15, blank=True, verbose_name=u'Номер телефона (моб.)')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    icq = models.CharField(max_length=15, blank=True, verbose_name=u'ICQ')
    skype = models.CharField(max_length=50, blank=True, verbose_name=u'Skype')

    def __unicode__(self):
        return self.name

    @property
    def lvl_verbose(self):
        return get_display(self.lvl, self.LVL)


class Restaurant(models.Model):
    FORM_COOP = (
        (u's', 'Standart'),
        (u'b', 'Buying'),
    )
    CITY = (
        (u'к', 'Киев'),
        (u'о', 'Киевская обл.'),
    )
    STATUS = (
        (u'б', 'Бизнес'),
        (u'п', 'Премиум'),
    )
    ORG_FORM = (
        (u'о', 'ООО'),
        (u'ф', 'ФОП'),
    )
    PAYMENT_TERM = (
        (u'п', '100% предоплаты'),
        (u'ч', '50%/50% в поточном месяце'),
        (u'н', 'Оплата постфактум'),
    )
    WARRANTY_MAIL = (
        (u'Н', 'Не требуется'),
        (u'п', 'Подписано'),
        (u'н', 'Не подписано'),
    )
    name_rus = models.CharField(max_length=100, verbose_name=u'Ресторан (рус.)')
    name_eng = models.CharField(max_length=100, blank=True, verbose_name=u'Ресторан (англ.)')
    form_coop = models.CharField(max_length=1, choices=FORM_COOP, verbose_name=u'Форма сотрудничества')
    chain_name_rus = models.CharField(max_length=100, verbose_name=u'Сеть ресторанов (рус.)')
    chain_name_eng = models.CharField(max_length=100, blank=True, verbose_name=u'Сеть ресторанов (англ.)')
    city = models.CharField(max_length=1, choices=CITY, verbose_name=u'Адрес')
    city_sec = models.CharField(max_length=50, blank=True)
    add_date = models.DateField(verbose_name=u'Дата создания')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u'Статус')
    site = models.URLField(blank=True, verbose_name=u'Сайт ресторана')
    org_form = models.CharField(max_length=1, choices=ORG_FORM, verbose_name=u'Организационная форма')
    details = models.TextField(verbose_name=u'Реквизиты')
    contact = models.ForeignKey(Contact, verbose_name=u'Контакт')
    payment_term = models.CharField(max_length=1, choices=PAYMENT_TERM, verbose_name=u'Условия оплаты')
    pay_term_com = models.TextField(blank=True, verbose_name=u'Комментарии к оплате')
    sum_payment = models.FloatField(verbose_name=u'Сумма оплаты')
    chain_avail = models.BooleanField(verbose_name=u'Наличие своей сети')
    equipment = models.BooleanField(verbose_name=u'Оборудование')
    plasma_all = models.IntegerField(blank=True, verbose_name=u'Общее количество плазм')
    plasma_work = models.IntegerField(blank=True, verbose_name=u'Количество подключенных плазм')
    contract = models.BooleanField(verbose_name=u'Договор')
    act_rec_trans = models.BooleanField(verbose_name=u'Акт приема передачи')
    list_restrict = models.BooleanField(verbose_name=u'Список ограничений')
    restriction = models.ManyToManyField(Branch, verbose_name=u'Ограничения')
    video = models.ManyToManyField(Video, verbose_name=u'Ролик')
    warranty_mail = models.CharField(max_length=1, choices=WARRANTY_MAIL, verbose_name=u'Гарантийное письмо на изображение физ. лица')
    stat_doc_1 = models.BooleanField()
    stat_doc_2 = models.BooleanField()
    stat_doc_3 = models.BooleanField()
    stat_doc_4 = models.BooleanField()

    class Meta:
        permissions = (
            ('view_name_rus', 'Название на русском'),
            ('view_name_eng', 'Название на английском'),
            ('view_form_coop', 'Форма сотрудничества'),
            ('view_chain_name_rus', 'Название сети на русском'),
            ('view_chain_name_eng', 'Название сети на английском'),
            ('view_city', 'Город'),
            ('view_add_date', 'Дата создания'),
            ('view_status', 'Статус'),
            ('view_site', 'Сайт'),
            ('view_org_form', 'Организационная форма'),
            ('view_details', 'Реквизиты'),
            ('view_contact', 'Контакт'),
            ('view_payment_term', 'Условия оплаты'),
            ('view_sum_payment', 'Сумма оплаты'),
            ('view_chain_avail', 'Наличие своей сети'),
            ('view_equipment', 'Оборудование'),
            ('view_plasma_all', 'Общее количество плазм'),
            ('view_plasma_work', 'Количество подключенных плазм'),
            ('view_contract', 'Договор'),
            ('view_act_rec_trans', 'Акт приема передачи'),
            ('view_list_restrict', 'Список ограничений'),
            ('view_restriction', 'Ограничения'),
            ('view_video', 'Ролик'),
            ('view_warranty_mail', 'Гарантийное письмо на изображение физ. лица'),
            ('view_stat_doc_1', 'stat_doc_1'),
            ('view_stat_doc_2', 'stat_doc_2'),
            ('view_stat_doc_3', 'stat_doc_3'),
            ('view_stat_doc_4', 'stat_doc_4'),
        )

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
