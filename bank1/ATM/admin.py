from django.contrib import admin
from ATM.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['username','password','pin','balance']

admin.site.register(Customer,CustomerAdmin)


# Register your models here.
