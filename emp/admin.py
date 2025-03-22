from django.contrib import admin
from .models import Employee,Department,Role

# Register your models here.
class Emoloyee_Admin(admin.ModelAdmin):
    list_display = ("first_name","last_name","phone_number")
admin.site.register(Employee,Emoloyee_Admin)
admin.site.register(Department)
admin.site.register(Role)