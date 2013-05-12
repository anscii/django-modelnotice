from django.contrib import admin
from models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'text', 'user', 'email')
    list_filter = ('content_type',)
    list_display_links = ('content_object','user')

admin.site.register(Notice, NoticeAdmin)
