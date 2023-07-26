from django.contrib import admin
from .models import Quotes

# Register your models here.
@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
  list_display = ['id','text','created_at','updated_at']
