from django.contrib import admin

from .models import Studentupdate
# Register your models here.
@admin.register(Studentupdate)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
