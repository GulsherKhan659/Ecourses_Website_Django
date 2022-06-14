from email.policy import default
from enum import unique
from random import random
from unicodedata import category
from django.db import models
import random
# Working on dynamic url after complete project
from autoslug import AutoSlugField

class AddCourseCategory(models.Model):
    print("Add Catergory")
    course_category = models.CharField(max_length=50)
    course_category_code = models.CharField(max_length=50,default=random.randint(00000,999999)+2)
    category_img = models.FileField(upload_to="catagory_img/",max_length=250,default=None,null=True)
    category_url = AutoSlugField(populate_from = 'course_category',unique=True,null=True,default=None)

class Courses(models.Model):
    listOFData=[]
    COURSE_LIST= tuple()
   
    try:
        data = AddCourseCategory.objects.all()
        categeries = [x.course_category for x in data ]
        indexes = [str(x) for x in range(1,len(data)+1) ]
        zipdata=  zip(indexes,categeries)
        COURSE_LIST =  tuple(zipdata)
    except:
        pass
           
    course_name = models.CharField(max_length=50)
    course_duration = models.CharField(max_length=50)
    course_rating = models.IntegerField()
    course_student = models.IntegerField()
    course_type =models.CharField(choices=COURSE_LIST,max_length=50,default="UnSelected")
    course_img = models.FileField(upload_to="course_img/",max_length=250,default=None,null=True)
    course_url = AutoSlugField(populate_from = 'course_name',unique=True,null=True,default=None)






# Create your models here.
