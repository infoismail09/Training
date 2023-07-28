from django.urls import path
from . import views

urlpatterns = [
    path('quotes/',views.quotes_list, name = 'quotes'),
    path('quotes/<int:pk>',views.quotes_details,name='quotes_details'),
    path('categories/',views.Categories_List.as_view()),
    path('categories/<int:pk>',views.Categories_details.as_view()),
    path('products/',views.ProductList.as_view(),name='Product_list'),
    path('product_create/',views.ProductCreate.as_view(),name='product_create'),
    path('product_retrive/<int:pk>/',views.ProductRetrieve.as_view(),name='product_retrive'),
    path('product_update/<int:pk>/',views.ProductUpdate.as_view(),name='product_update'),
    path('product_delete/<int:pk>/',views.ProductDelete.as_view(),name='product_delete'),
    # generics combination concrete url end points
    path('product_list_create/',views.ProductListCreate.as_view(),name='product_list_create'),
    path('product_retrive_update/<int:pk>/',views.ProductRetriveUpdate.as_view(),name='product_retrive_update'),
    path('Products/Delete/<int:pk>/',views.ProductRetriveDestroy.as_view(),name='Delete_Products'), # as per the below naming convention taken api end point
    path('Products/RetrieveUpdateDestroy/<int:pk>/',views.ProductRetrieveUpdateDestroy.as_view(),name='RetrieveUpdateDestroy'),
    #### Creating endpoint for nested serializers concept

]   


# Naming Api conventions
# GET /products
# POST /products

# GET /products/:id
# PUT /products/:id
# PATCH /products/:id
# DELETE /products/:id

# DELETE /products/:id/