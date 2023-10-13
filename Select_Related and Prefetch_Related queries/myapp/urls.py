from django.urls import path
from . import views

urlpatterns = [
    path('select_related/', views.select_related_view, name='select_related'),
    path('prefetch_related/', views.prefetch_related_view, name='prefetch_related'),
    path('author_books/<int:author_id>/', views.author_books, name='author_books'),
    path('prolific_authors/', views.prolific_authors, name='prolific_authors'),
    path('books_and_authors/', views.books_and_authors, name='books_and_authors'),
]

