from django.contrib import admin
from index.models import Video


class VideoAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address')
    list_display = ('name', 'address', 'start_date', 'end_date')
    readonly_fields = ('periodicity', )


admin.site.register(Video, VideoAdmin)
