from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song
from django.db.models import Count, Min, Max, Sum, Avg
from django.db.models import Q

# Create your views here.


def get_album(request):
    # details=Album.objects.all()
    # details=Album.objects.get(id=1) terminal pe milega but varialbe nahi lena and get se query nahi milegi
    # details=Album.objects.filter(genre="Action")
    # details=Album.objects.exclude(genre="Action,Drama")
    # details=Album.objects.exclude(artist="hritik")
    # details=Album.objects.exclude(artist="Ramcharan").exclude(genre="comedy")

    # agrregate ORM

    # details=Album.objects.count() # no .query
    # details=Album.objects.annotate(Min("awards"))
    # print(details)  # creates a seperate summury of queryset
    # details=Album.objects.annotate(Max("awards"))
    # details=Album.objects.order_by("title") #ascending order
    # details=Album.objects.order_by("-title") #DESCENDING 0RDER
    # details=Album.objects.order_by("?") #random order
    # details=Album.objects.exclude(genre='action')  # Dont include this genre

    # modify the existing query
    # details=Album.objects.get(id=11)
    # details.genre="Biography"
    # details.save()
    # print(details)

    # details=Album.objects.order_by("id").reverse()[:3]
    # details=Album.objects.values()
    # print(details)

    # details=Album.objects.values('title','awards')
    # details=Album.objects.values_list("awards", flat=True)
    # print(details)

    # details=Album.objects.distinct()
    # print(details.query)

    # details=Album.objects.exists()
    # print(details)

    # details=Album.objects.first()
    # details=Album.objects.last()
    # details=Album.objects.latest("awards")
    # details=Album.objects.earliest("title")

    # create orm query
    # details = Album(title="mission majnu",artist="shidhart Malhotra",genre='action',awards=67)
    # details.save()
    # print(details) # .query method is not allowed 

    # bulk create orm query
    # data=[Album(title="baban Singh",artist="anil Kapoor",genre="Drama",awards=9),
    # Album(title="mission rangigang",artist="akshay kumar",genre="biography",awards=16),
    # Album(title="deth squad",artist="john cena",genre="funny movie",awards=20)]
    # details=Album.objects.bulk_create(data)
    # print(details)

    # details=Album.objects.get_or_create(title="krissh",artist="hritik",genre="action",awards=15)
    # print(details)

    # get or create functionality

    # try:
    #     details = Album.objects.get(title='Leo Tolstoy',artist="leonardo",genre="comedy",awards=8)
    # except:
    #     Album.objects.exists()
    #     details = Album(title='Leo Tolstoy',artist="leonardo",genre="comedy",awards=8)
    #     details.save()
    # print(details)

    # details,created=Album.objects.update_or_create(id=14,title="war",defaults={'title':'krissh'})
    # details=Album.objects.all()
    # for album in details:
    #     album.genre="Movies"
    # details_album=Album.objects.bulk_update(details,['genre'])
    # details=Album.objects.in_bulk()
    # details=Album.objects.all()
    # print(details.count())
    # details=Album.objects.aggregate(Max("awards"))
    # details=Album.objects.aggregate(Min("awards"))
    # details=Album.objects.aggregate(Avg("awards"))
    # details=Album.objects.aggregate(Sum("awards"))
    # details=Album.objects.aggregate(Count("awards"))
    # details=Album.objects.filter(genre__exact="action")
    # details = Album.objects.annotate(num_books=Count('genre'))
    # details=Album.objects.filter(genre__iexact="Action")
    # details=Album.objects.filter(awards__lt=20)
    # details=Album.objects.filter(awards__gte=20)
    # details = Album.objects.filter(awards__gt=20).values()   # it vill give you dictnary key way of fields
    # details=Album.objects.filter(artist__contains="hritik")
    # details=Album.objects.filter(artist__startswith="R")
    # details=Album.objects.filter(title__startswith=1)
    # details=Album.objects.filter(artist__endswith="r")
    # details = Album.objects.defer('title')
    # details = Album.objects.only('genre')

    # And operater orm

    # details = Album.objects.filter(genre="action") & Album.objects.filter(artist="Rohit shetty")
    # print(details)

    # details = Album.objects.filter(genre="action").filter(artist="Rohit shetty")
    # print(details)


    # OR (|)

    # details = Album.objects.filter(genre="action") | Album.objects.filter(artist="Rohit shetty")
    # print(details)

    # details = Album.objects.filter(Q(genre="action")|Q(artist="Rohit shetty"))
    # print(details)


    # XOR (^)

    # details = Album.objects.filter(genre="action") ^ Album.objects.filter(artist="Rohit shetty")
    # print(details)

    # details = Album.objects.filter(Q(genre="action") ^ Q(artist="Rohit shetty"))
    # print(details)


    # bul_ create nomal way

    # data=[Album(title="Kabir Singh",artist="Sahid Kapoor",genre="Romantic",awards=7),
    # Album(title="shershah",artist="Sidhdharth",genre="Biography",awards=14),
    # Album(title="URI",artist="Vicky Kaushal",genre="biography",awards=20)]
    # details=Album.objects.bulk_create(data)

     # to retrive data

    # details=Album.objects.get(id=1)   # dont use .query bcz single object show karne me capeble hai 
    # details=Album.objects.get(id=2)
    # details=Album.objects.get(id=3)
    # details=Album.objects.get(id=11)
    # print(details)

    # ## create 
    # details = Album(title="Marvel Avengers",artist="iron man",genre="Action",awards="12")
    # details.save()
    # print(details)

    # ##  update
    # details = Album.objects.get(id=2)
    # details.genre="pop"
    # details.save()
    # print(details)

    # details = Album.objects.get(id=12)
    # details.genre="Romace"
    # details.artist="Sharuk Khan"
    # details.title="Glass"
    # details.save()
    # print(details)

    ## delete 
    # details = Album.objects.get(id=4)
    # details.delete()
    # print(details.query)

    ## to delete multiple objects

    # details= Album.objects.filter(genre="pop").delete()
    # print(details)

######### Bulk Create functionality ############


    # data = [
    #     {
    #         "title": "kabir sing",
    #         "artist": "sahid kapoor",
    #         "genre": "Action",
    #         "award": "7",
    #     },
    #     {
    #         "title": "ing",
    #         "artist": "sahid ",
    #         "genre": "Comedy",
    #         "award": "0",
    #     },
    # ]
    # list_of_objects = []

    # for i in data:
    #     list_of_objects.append(
    #         Album(
    #             title=i["title"],
    #             artist=i["artist"],
    #             genre=i["genre"],
    #             awards=i["award"],
    #         )
    #     )

    # Album.objects.bulk_create(list_of_objects)
    # print(details)
    # print()
    # print(details.query)

    ### bulk update 

    # new_title = "Shazam comics"
    # new_artist = "Batman"
    # new_genre = "Action"
    # new_awards = "Silver"

    # instances_to_update = Album.objects.filter(id__in=[11,12,13])
    

    # for instance in instances_to_update:
    #     instance.title = new_title
    #     instance.artist = new_artist
    #     instance.genre = new_genre
    #     instance.awards = new_awards

    # Album.objects.bulk_update(instances_to_update,fields=['title','artist','genre','awards'])


    return HttpResponse(
        "<h1>Welcome to My Object Relational Mapping <br>Album</br></h1>"
    )


def get_song(request):
    # song_data = Song.objects.all()
    # song_data = Song.objects.count()
    # print(song_data)
    # details = Song.objects.select_related("album").all()
    # print(details)
    return HttpResponse(
        "<h1>Welcome to My Object Relational Mapping <br>Song</br></h1>"
    )
