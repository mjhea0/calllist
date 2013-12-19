from django.contrib import admin
from tocall.models import Contact, History

# class HistoryInline(admin.StackedInline):
# 	fieldsets = [
# 		(None, {'fields': ['contact', 'write_up', 'cntacted_at']}),
# 		('Details', {
# 			'classes': ['collapse',],
# 			'fields': ['email_in', 'email_out', 'email_linkedin',
# 			'call_in', 'call_out', 'voice_mail', 'message', 'no_message',
# 			'no_answer', 'meeting']
# 			})

# 	]

class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['first_name', 'last_name']}),
		('Next communication', {
			'fields': ['next_call', 'note', 'user']
		}),
		('Reach', {
			'classes': ['collapse',],
			'fields': ['email', 'mobile', 'office']
		}),
		('Work', {
			'classes': ['collapse',],
			'fields': ['role', 'company', 'url', 'introduced_by']
		}),
		('Change History', {
			'classes': ['collapse',],
			'fields': ['created_at', 'updated_at']
		})
	]
	readonly_fields = ('created_at', 'updated_at')
	# inlines = [HistoryInline]

	# list_display = ('__unicode__', '')

admin.site.register(Contact, ContactAdmin)

