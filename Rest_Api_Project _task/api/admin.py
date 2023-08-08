from django.contrib import admin
from .models import Quotes,Categories,Products,FAQs

# Register your models here.
@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
  list_display = ['id','text','created_at','updated_at']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
  list_display = ['id','title','created_at','updated_at']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
  list_display = ['id','title','created_at','updated_at']

@admin.register(FAQs)
class Faqsadmin(admin.ModelAdmin):
  list_display = ['id','questions','answer','attachment']