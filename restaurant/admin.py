from django.contrib import admin
from restaurant.models import Contact, Restaurant


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'phone_work', 'email')


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ('name_rus', 'name_eng')
    list_display = ('name_rus', 'name_eng', 'city', 'add_date')
    filter_horizontal = ('restriction', )


admin.site.register(Contact, ContactAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
