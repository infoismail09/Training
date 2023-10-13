from django.shortcuts import render
from .models import Author,Book
# Create your views here.

# Suppose you want to retrieve all the books authored by a specific author,
# and you want to select related author information efficiently. Here's how you can do it:

def select_related_view(request):
    books = Book.objects.select_related('author').all() 
    return render(request,'book_list.html',{'books':books})


#Suppose you want to retrieve all authors who have written more than five books 
# and display their books. Here's how you can do it using prefetch_related:

def prefetch_related_view(request):
    authors = Author.objects.prefetch_related('book_set').all()
    return render(request,'author_list.html',{'authors':authors})


################# more advanced queries ####################

#Suppose you want to retrieve all the books authored by a specific author,
# and you want to select related author information efficiently. Here's how you can do it:

def author_books(request, author_id):
    author_books = Book.objects.select_related('author').filter(author_id=author_id)
    return render(request, 'author_books.html', {'author_books': author_books})


#Using prefetch_related for More Advanced Queries:

#Suppose you want to retrieve all authors who have written more than five books
#  and display their books. Here's how you can do it using prefetch_related:

def prolific_authors(request):
    prolific_authors = Author.objects.annotate(book_count=Count('book')).filter(book_count__gt=5).prefetch_related('book_set')
    return render(request, 'prolific_authors.html', {'prolific_authors': prolific_authors})


#Using select_related and prefetch_related Together:

#You can also use select_related and prefetch_related together in more complex scenarios. For example, if you want to display a list of books with their authors, 
# and you want to optimize the query to reduce database hits:

def books_and_authors(request):
    books = Book.objects.select_related('author').prefetch_related('author__book_set')
    return render(request, 'books_and_authors.html', {'books': books})





