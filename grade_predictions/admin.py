from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student


admin.site.register(Student, StudentAdmin)
admin.site.register(GrUser)
admin.site.register(Subject)
admin.site.register(Career)
admin.site.register(Teacher)

# Register your models here.
