from django.contrib import admin
from .models import Detail, Contact, Member

# Register your models here.

#class DetailAdmin(admin.ModelAdmin):
 #     list_display = ("name", "phone",)

#class ContactAdmin(admin.ModelAdmin):
#      list_display = ("name", "email", )   

#class MemberAdmin(admin.ModelAdmin):
#      list_display = ("name", "phone", )         
  
admin.site.register(Detail)
admin.site.register(Contact)
admin.site.register(Member)