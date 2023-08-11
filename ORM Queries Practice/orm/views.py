from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song
from django.db.models import Count, Min, Max, Sum, Avg

# Create your views here.


def get_album(request):
    # details=Album.objects.all()
    # details=Album.objects.get(pk=1)
    # details=Album.objects.filter(genre="Action")
    # details=Album.objects.exclude(genre="Action,Drama")
    # details=Album.objects.exclude(artist="hritik")
    # details=Album.objects.exclude(artist="Ramcharan").exclude(genre="comedy")
    # details=Album.objects.get(id=1)
    # details.awards=10
    # details=Album.objects.get(id=2)
    # details.awards=25
    # details=Album.objects.get(id=3)
    # details.awards=15
    # details=Album.objects.get(id=4)
    # details.awards=40
    # details.save()
    # details=Album.objects.count()
    # details=Album.objects.annotate(Min("awards"))
    # details=Album.objects.annotate(Max("awards"))
    # print(vars(details[0]))
    # details=Album.objects.order_by("title") #ascending order
    # details=Album.objects.order_by("-title") #DESCENDING 0RDER
    # details=Album.objects.order_by("?") #random order
    # details=Album.objects.exclude(genre='action')  # Dont include this genre
    # details=Album.objects.get(id=2)
    # details.save()
    # details=Album.objects.get(id=3)
    # details.genre="Biography"
    # details.save()
    # details=Album.objects.order_by("id").reverse()[:3]
    # details=Album.objects.values()
    # details=Album.objects.values('title','awards')
    # details=Album.objects.values_list("", flat=True)
    # details=Album.objects.distinct("title")
    # details=Album.objects.exists()
    # details=Album.objects.first()
    # details=Album.objects.last()
    # details=Album.objects.latest("awards")
    # details=Album.objects.earliest("title")
    # details=Album.objects.create(title="gadar",artist="sunny deol",genre="action",awards=23)
    # data=[Album(title="Kabir Singh",artist="Sahid Kapoor",genre="Romantic",awards=7),
    # Album(title="shershah",artist="Sidhdharth",genre="Biography",awards=14),
    # Album(title="URI",artist="Vicky Kaushal",genre="biography",awards=20)]
    # details=Album.objects.bulk_create(data)
    # details=Album.objects.get_or_create(title="krissh",artist="hritik",genre="action",awards=15)
    # details=Album.objects.get_or_create(title="1983",artist="Ranveer Singh",genre="Sports",awards=16)
    # details=Album.objects.filter(id=3).update(genre="action")
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
    # details=Album.objects.filter(genre__exact="action")
    # details = Album.objects.annotate(num_books=Count('genre'))
    # details=Album.objects.filter(genre__iexact="Action")
    # details=Album.objects.filter(awards__lt=20)
    # details=Album.objects.filter(awards__gte=20)
    # details=Album.objects.filter(artist__contains="hritik")
    # details=Album.objects.filter(artist__startswith="R")
    # details=Album.objects.filter(title__startswith=1)
    # details=Album.objects.filter(artist__endswith="r")
    # details = Album.objects.defer('title')
    # details = Album.objects.only('genre')

    # data=[Album(title="Kabir Singh",artist="Sahid Kapoor",genre="Romantic",awards=7),
    # Album(title="shershah",artist="Sidhdharth",genre="Biography",awards=14),
    # Album(title="URI",artist="Vicky Kaushal",genre="biography",awards=20)]
    # details=Album.objects.bulk_create(data)

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


    data = [
        {"name": "honey sing", "album": "yo yo honey singh"},
        {"name": "Meka", "album": "tara raha "},
    ]
    album_instance=Album.objects.get(id=9)

    list_of_objects = []

    for i in data:
        list_of_objects.append(Song(name=i["name"], album=album_instance))

        Song.objects.bulk_create (list_of_objects)

    # print(details)
    # print()
    # print(details.query)

    return HttpResponse(
        "<h1>Welcome to My Object Relational Mapping <br>Album</br></h1>"
    )


def get_song(request):
    song_data = Song.objects.all()
    song_data = Song.objects.count()
    details = Song.objects.select_related("album").all()
    print(details)
    return HttpResponse(
        "<h1>Welcome to My Object Relational Mapping <br>Song</br></h1>"
    )
