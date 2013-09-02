from django.contrib import admin
from client.models import Client, Contact, AdvertisingCampaign


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'phone_work', 'email')


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'add_date')


class AdvertisingCampaignAdmin(admin.ModelAdmin):
    search_fields = ('client', )
    list_display = ('client', 'subject', 'video')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(AdvertisingCampaign, AdvertisingCampaignAdmin)
