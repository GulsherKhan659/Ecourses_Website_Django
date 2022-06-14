from django.contrib import admin
from teachers.models import Teacher

class TeacherAdmin(admin.ModelAdmin):
      list_display= ('teacher_name','teacher_subject','teacher_qualification','teacher_pic')
      

admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
