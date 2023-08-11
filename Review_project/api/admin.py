from django.contrib import admin
from .models import Company,Branch
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ['id','name']

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
  list_display = ['id','address','company']