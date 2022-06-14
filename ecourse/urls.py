"""ecourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecourse import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="home"),
    path('about', views.about_page, name="about"),
    path('teacher', views.teacher_page, name="teachers"),
    path('course', views.course_page, name="courses"),
    path('blog', views.blog_page, name="blog"),
    path('contact', views.contact_page, name="contact"),
    path('practice/<myid>',views.practice,name="practice"),
    path('course-details/<id>',views.course_details),
    path('course-by-catagory/course-details/<id>',views.course_details),
    path('course-by-catagory/<id>',views.courses_by_categories),
    path('view-courses',views.all_courses),
    
    path('view-catagories',views.all_categories)

]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
        
    
    