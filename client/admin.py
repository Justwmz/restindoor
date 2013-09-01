from django.contrib import admin
from client.models import Client, Contact, AdvertisingCampaign


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'phone_work', 'email')


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name_rus', )
    list_display = ('name_rus', 'name_eng', 'add_date', 'control')


class AdvertisingCampaignAdmin(admin.ModelAdmin):
    search_fields = ('client', )
    list_display = ('client', 'subject', 'video')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(AdvertisingCampaign, AdvertisingCampaignAdmin)
