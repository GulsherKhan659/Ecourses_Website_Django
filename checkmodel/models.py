
from django.db import models

class CheckFields(models.Model):
    all_choices = (
        ("1","English"),
        ("2","Urdu"),
        ("3","Punjabi"),
        ("4","German")
        )
    
    choice = models.CharField(choices=all_choices,max_length=50,default="Select Language")
    
#     def __str__(self) :
#         return self.all_choices
# # Create your models here.
