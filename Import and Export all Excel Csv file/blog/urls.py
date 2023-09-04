from django.urls import path
from . import views


urlpatterns = [
    path('export_data_to_excel/',views.export_data_to_excel),
    path('import_data_to_db/',views.import_data_to_db),
]