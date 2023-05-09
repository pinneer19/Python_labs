from django.contrib import admin
from .models import Department, Doctor, Specialization

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Specialization)
