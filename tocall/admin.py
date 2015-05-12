from django.contrib import admin
from tocall.models import Contact, History


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['contact', 'write_up', 'contacted_at']}),
        ('Details', {
            'classes': ['collapse', ],
            'fields': ['email_in', 'email_out', 'email_linkedin',
                       'call_in', 'call_out', 'voice_mail', 'message',
                       'no_message', 'no_answer', 'meeting']
            })
    ]
    readonly_fields = ('contacted_at',)
    list_display = ('id', 'contact', 'write_up', 'contacted_at')
    search_fields = ['write_up']


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name']}),
        ('Next communication', {
            'fields': ['next_call', 'note', 'user']
        }),
        ('Reach', {
            'classes': ['collapse', ],
            'fields': ['email', 'mobile', 'office']
        }),
        ('Work', {
            'classes': ['collapse', ],
            'fields': ['role', 'company', 'url', 'introduced_by']
        }),
        ('Change History', {
            'classes': ['collapse', ],
            'fields': ['created_at', 'updated_at']
        })
    ]
    readonly_fields = ('created_at', 'updated_at')

    list_display = ('id', 'first_name', 'last_name', 'next_call')

admin.site.register(Contact, ContactAdmin)
admin.site.register(History, HistoryAdmin)
