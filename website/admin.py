from django.contrib import admin

from website.models import contact, Newsletter

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display = ['name','email' , 'created_date']
    list_filter = ['email']
    search_fields = ['name' , 'message']
admin.site.register(contact , contactAdmin)

admin.site.register(Newsletter)
