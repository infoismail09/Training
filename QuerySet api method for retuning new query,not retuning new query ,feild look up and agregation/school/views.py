from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
from datetime import date,time
# Create your views here.

def home(request):
    # student_data = Student.objects.all()
    
    # student_data = Student.objects.filter(marks=70)

    # student_data = Student.objects.exclude(marks=70)

    # student_data = Student.objects.order_by("city")
    # student_data = Student.objects.order_by("marks")
    # student_data = Student.objects.order_by("?")
    # student_data = Student.objects.order_by("name")  # it vill follow uicode value of character caps A and small A letter
    # student_data = Student.objects.order_by("id")
    # student_data = Student.objects.order_by("-id")
    # student_data = Student.objects.order_by("id").reverse()
    # student_data = Student.objects.order_by("id").reverse()[:5]

    # student_data = Student.objects.values() # it will give query set in terminal as list of disctionay
    # student_data = Student.objects.values("name")
    # student_data = Student.objects.values("name","city")
    # student_data = Student.objects.values_list() # it will show data in tuple format that is query set
    # student_data = Student.objects.values_list("id","name", named=True) # it will show id and name in tuple format and when add named = True then it will reflect on browser as well

    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates("pass_date","month") # distict data of month
    # student_data = Student.objects.dates("pass_date","year") # data will show in terminal bcz it will be in tuple also show distinct data
     #  feild it shouls be Datefield 
    # kind it should either "year","month","week","or day"
    # order it should either Asc or DESC by defalut ASC

    # student_data = Student.objects.none() # it will show empty query set.

    ############## Query set with Second Table Started ################
    # union Example if multiple same data wil there then it will show only 1 data not also if smae data replicte in in same tabe it will show that data 
    # note to perform unionsame colom shound be taken 3x3 other wise error

    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)                                  

    # student_data = qs2.union(qs1,all=True)  # it will shoe all data even if duplicate data is available like same name of techer and student 

    # Intersection Example:- it is uded with 2 or more table and it will applicable with union as well

    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)                                  

    # student_data = qs2.intersection(qs1)

    # Diffrence Example:

    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Teacher.objects.values_list('id','name',named=True)                                  

    # student_data = qs2.difference(qs1) # note jisse hum difrence lenge uska hi data ayega compare ho ke student -  techer 

######## ORM Operator queries ##########
# & operator 

    # student_data = Student.objects.filter(id=10) & Student.objects.filter(roll=109)

    # student_data = Student.objects.filter(id=9,roll=108) # another way of writing & operator query

    # student_data = Student.objects.filter(Q(id=9) & Q(roll=108)) # another way of writing & operator # query dont forget to to import Q 

# | operator ORm Query

    # student_data = Student.objects.filter(id=7) | (roll=108)

    # student_data = Student.objects.filter(Q(id=5) | Q(roll=108)) # another way of writing | operator # query dont forget to to import Q 

  ####### query set that does not retun any query set ###############  

    # student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.get(name="Naeem") # if name repeat agaiin multiple object retun exeption will retun so please lookn up uniquely identify coloum

    # student_data = Student.objects.first() # order by prmary key

    # student_data = Student.objects.order_by('name').first()  

    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date') # it required positionall agument like pass_date,name any feild

    # student_data = Student.objects.all()
    # print(student_data.exists())    # it give you true if data is present it will show in terminal.

    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    # student_data = Student.objects.create(name="sameer",roll=114,
    #                                       city="jharkhand",marks=60,pass_date="2020-5-4") # create and save directly using view

    # student_data,created = Student.objects.get_or_create(name="anisha",roll=115,
    #                                       city="jharkhand",marks=60,pass_date="2020-5-4") # isme agar data rahega toh fetch karega and toh new data create kar dega but fiels unique rakhini hhai
    
    # print(created)


    # student_data = Student.objects.filter(id=6).update(name="kabir",marks=80) # in the terminal it show isne kitna data update kia hai like return 1 and browser pe data nahi dekhega 

# imortent not that ki get sisf object return karta hai and filter method query set return karta hai (query set :- it is a list of oobject of a given model tht allow us to read data from database.)

    # multiple update 

    # student_data = Student.objects.filter(marks=60).update(city="pass")

    # student_data = Student.objects.update_or_create(id=15,name="sameer",roll=115 defaults={"name":"kholi"})  # isme agar data nahi hai to create hoga to update karega nahi hoga to reate karega and imp not null value liya hai fiels me toh wo lena ja roori hai 
    # print(created)

    # bulk create # it will nit work with many to many relation ship
    
    # objs = [
    #     Student(name="Atif",roll=116,city="Dhanbad",marks=70,pass_date="2020-5-4"),
    #     Student(name="sahil",roll=117,city="kanpur",marks=80,pass_date="2020-6-4"),
    #     Student(name="Taufiq",roll=118,city="lakhnow",marks=50,pass_date="2020-7-4"),
    # ]

    # student_data = Student.objects.bulk_create(objs)

   # bulk update 

#    all_student_data = Student.objects.all()
#    for stu in all_student_data:
#     stu.city = "Mumbai"
#     student_data = Student.objects.bulk_update(all_student_data,['city'])

    # in bulk

    # student_data = Student.objects.in_bulk([1,2])
    # print(student_data[1].name) # it will show data in terminal 

    # student_data = Student.objects.in_bulk([]) # agar hum isse blank rakhe toh terminal pe retun { } pshoe karta hai

    # student_data = Student.objects.in_bulk() # ye hame sab object de dega terminal me 

# delete 

    # student_data = Student.objects.get(pk=12).delete() # single opbject delete

# bulk Delete

    # student_data = Student.objects.filter(marks=60).delete()

# sub deete karna hai toh simple type
#  
    # student_data = Student.objects.all().delete()

    # student_data = Student.objects.all()

    # print(student_data.count())

############### feild lookup in orm queries ########### in this for loop will use in templates with add ed feild admdatetime

    # student_data = Student.objects.filter(name__exact="Ismail")

    # student_data = Student.objects.filter(name__iexact="Ismail") # ye case sensetive hai isme agar small letter se ismail likha toh bhi show karega 

    # student_data = Student.objects.filter(name__contains="Naeem")

    # student_data = Student.objects.filter(name__contains="N")

    # student_data = Student.objects.filter(name__icontains="N")

    # student_data = Student.objects.filter(id__in = [1,5,7]) 

    # student_data = Student.objects.filter(marks__in = [50])

    # student_data = Student.objects.filter(marks__in = [50,70])

    # student_data = Student.objects.filter(marks__gt = 60) # gt stand for greaten then 

    # student_data = Student.objects.filter(marks__gte = 60) # stands for greater then equal 2

    # student_data = Student.objects.filter(marks__lt = 60) # ltstands for less then 

    # student_data = Student.objects.filter(marks__lte = 60)

    # student_data = Student.objects.filter(name__startwith='R')

    # student_data = Student.objects.filter(name__istartwith='R')

    # student_data = Student.objects.filter(name__endswith='l')

    # student_data = Student.objects.filter(name__iendswith='l')

    # student_data = Student.objects.filter(pass_date__range=('2020-04-01','2020-05-10'))

    # student_data = Student.objects.filter(amddatetime__date=date(2020,6,5))

    # student_data = Student.objects.filter(amddatetime__date__gt=date(2020,6,5))

    # student_data = Student.objects.filter(pass_date__year=2020)

    # student_data = Student.objects.filter(pass_date__year__gte=2020)

    # student_data = Student.objects.filter(pass_date__month=5)

    # student_data = Student.objects.filter(pass_date__month__gte=5)

    # student_data = Student.objects.filter(pass_date__day=2)

    # student_data = Student.objects.filter(pass_date__day__lte=13)

    # student_data = Student.objects.filter(pass_date__week=2)

    # student_data = Student.objects.filter(pass_date__week_day=1)

    # student_data = Student.objects.filter(pass_date__quarter=3)

    # student_data = Student.objects.filter(admdatetime__time__gt=time(6,00))

    # student_data = Student.objects.filter(admdatetime__time__gt=time(2,17))

    # student_data = Student.objects.filter(admdatetime__hour__gt=5)

    # student_data = Student.objects.filter(admdatetime__minute__gt=26)

    # student_data = Student.objects.filter(admdatetime__second__lt=36)

    # student_data = Student.objects.filter(roll__isnull=True)

    student_data = Student.objects.filter(roll__isnull=False)

    print("Return:",student_data)
    print()
    print("SQL Query:",student_data.query)
    # return render (request,"school/index.html",{'students':student_data}) # this is used for retuning query set
    # return render (request,"school/index.html",{'student':student_data}) # thsi is used for not retuning query set
    return render (request,"school/feild.html",{'student':student_data})

