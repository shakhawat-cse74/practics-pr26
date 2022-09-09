from django.contrib import admin
from enroll.models import Student
# Register your models here.

#admin.site.register(Student, StudentAdmin)
# Use Decore
@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','stuid','stuname','stuemail','stupass')


