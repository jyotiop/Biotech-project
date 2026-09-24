from django.contrib import admin
from .models import Admin, Student, Login, Enquiry

# Register your models here.
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Enquiry)

