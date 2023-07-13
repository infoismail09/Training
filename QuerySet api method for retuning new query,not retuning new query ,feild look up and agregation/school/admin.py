from django.contrib import admin
from .models import Student,Teacher

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ["id","name","roll","city","marks","pass_date"]


@admin.register(Teacher)
class Teacheradmin(admin.ModelAdmin):
    list_display = ["id","name","empnum","city","join_date"]