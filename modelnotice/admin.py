from django.contrib import admin
from models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'text', 'user', 'email')
    list_display_links = ('content_object',)

admin.site.register(Notice, NoticeAdmin)
