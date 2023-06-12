from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Movie

# Create your views here.
# function to show all movies data 

def index(request):
    Movies = Movie.objects.all()
    # output = ','.join([m.title for m in Movies]) the following code used to reflec the movies name 
    # return HttpResponse(output)
    return render(request,'movies/index.html',{'movies':Movies})

# function to show details of movies with exception handaling if record not avalaibleit will show 404 page not found

# def detail(request, movie_id):
#     try:
#       movie = Movie.objects.get(pk=movie_id)
#     # return HttpResponse(movie_id) this is used to fetch the data of single object 
#       return render(request, 'movies/details.html',{'movie':movie})
#     except Movie.DoesNotExist:
#        raise Http404


# another way to show 404 page not found is :-

def detail(request, movie_id):       
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request,'movies/details.html',{'movie':movie})
