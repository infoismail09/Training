from django.urls import path
from . import views

urlpatterns = [
    path('companies/',views.company_list, name='companylistcreate'),
    path('companies/<int:pk>/',views.CompaniesDetails.as_view(),name='companiesDetails'),
]