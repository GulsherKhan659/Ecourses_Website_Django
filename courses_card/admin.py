from django.contrib import admin
from courses_card.models import  Courses,AddCourseCategory

class CourseCard(admin.ModelAdmin):

    list_display=('course_name','course_duration','course_rating','course_student','course_type')
    
    
admin.site.register(Courses,CourseCard)
admin.site.register(AddCourseCategory)
# Register your models here.
