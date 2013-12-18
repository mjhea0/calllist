from django.contrib import admin
from tocall.models import Contact

admin.site.register(Contact)

# class ContactAdmin(admin.ModelAdmin):
# 	list_display = ('__unicode__', '')