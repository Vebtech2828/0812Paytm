from django.contrib import admin
from Online_Payments.models import employee

class employeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']


admin.site.register(employee,employeeAdmin) # Comma was missing

