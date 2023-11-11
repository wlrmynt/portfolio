from django.contrib import admin
from .models import Detail, Contact

# Register your models here.

class DetailAdmin(admin.ModelAdmin):
      list_display = ("name", "phone", )

class ContactAdmin(admin.ModelAdmin):
      list_display = ("name", "email", )      
  
admin.site.register(Detail, DetailAdmin)
admin.site.register(Contact, ContactAdmin)