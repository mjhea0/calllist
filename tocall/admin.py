from django.contrib import admin
from tocall.models import Contact

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

	# list_display = ('__unicode__', '')

admin.site.register(Contact, ContactAdmin)
