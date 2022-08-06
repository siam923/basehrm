from django.contrib import admin
from .models import Employee, L_DAY_COUNT, LeaveForm
# Register your models here.
admin.site.register(Employee)
admin.site.register(L_DAY_COUNT)
admin.site.register(LeaveForm)