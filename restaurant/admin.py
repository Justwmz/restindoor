from django.contrib import admin
from restaurant.models import Contact, Branch, Video, Restaurant


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'phone_work', 'email')


class BranchAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', )


class VideoAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address')
    list_display = ('name', 'address', 'start_date', 'end_date')
    readonly_fields = ('periodicity', )


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ('name_rus', 'name_eng')
    list_display = ('name_rus', 'name_eng', 'city', 'add_date')
    filter_horizontal = ('restriction', 'video')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
