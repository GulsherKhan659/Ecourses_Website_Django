from django.db import models

class Teacher(models.Model):
      teacher_name    = models.CharField(max_length=50)
      teacher_subject = models.CharField(max_length=50)
      teacher_qualification= models.CharField(max_length=50,null=True)
      teacher_pic = models.FileField(upload_to="teacher_img/",max_length=250,null=True)
      

# Create your models here.
