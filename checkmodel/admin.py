from django.contrib import admin
from checkmodel.models import CheckFields

class AdminModel(admin.ModelAdmin):
      pass   

admin.site.register(CheckFields)

# Register your models here.
