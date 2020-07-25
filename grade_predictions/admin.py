from django.contrib import admin
from .models import *
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student


class SubjectAdmin(TreeNodeModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION

    form = TreeNodeForm


admin.site.register(Student, StudentAdmin)
admin.site.register(GrUser)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Career)
admin.site.register(Teacher)

# Register your models here.
