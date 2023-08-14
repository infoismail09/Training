from django.urls import path
from . import views
# from django.views.decorators.cache import cache_page


urlpatterns = [
    path('quotes/',views.quotes_list, name = 'quotes'),
    # path('quotes/<int:pk>',views.quotes_details,name='quotes_details'),
    path('categories/',views.Categories_List.as_view()),
    # creating Endpoint for filter and search
    # path('categorygetapi/',views.Category_list.as_view()),
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
    # now for task creating endpoint for categoy list and product list
    # path('categorygetapi/',views.Category_list.as_view()),
    # path('productgetapi/',views.Category_list.as_view()),
    path('faqslistcreate/',views.FaqsListCreate.as_view(),name='FaqsListCreate'),
    path('faqsRetrieveUpdateDestroy/<int:pk>/',views.RetrieveUpdateDestroyFaqs.as_view(),name='RetriveUpdateDestroy'),
    # for cache example for perview cache
    # path('faqsRetrieveUpdateDestroy/<int:pk>/',cache_page(1800)(views.RetrieveUpdateDestroyFaqs.as_view()),name='RetriveUpdateDestroy'),
    
]   


# Naming Api conventions
# GET /products
# POST /products

# GET /products/:id
# PUT /products/:id
# PATCH /products/:id
# DELETE /products/:id

# DELETE /products/:id/