from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
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

    qs1 = Student.objects.values_list('id','name',named=True)
    qs2 = Teacher.objects.values_list('id','name',named=True)                                  

    student_data = qs2.difference(qs1) # note jisse hum difrence lenge uska hi data ayega compare ho ke student -  techer 

######## ORM Operator queries ##########
# & operator 

    # student_data = Student.objects.filter(id=10) & Student.objects.filter(roll=109)

    # student_data = Student.objects.filter(id=9,roll=108) # another way of writing & operator query

    # student_data = Student.objects.filter(Q(id=9) & Q(roll=108)) # another way of writing & operator # query dont forget to to import Q 

# | operator ORm Query

    # student_data = Student.objects.filter(id=7) | (roll=108)

    student_data = Student.objects.filter(Q(id=5) | Q(roll=108)) # another way of writing | operator # query dont forget to to import Q 


    print("Return:",student_data)
    print()
    print("SQL Query:",student_data.query)
    return render (request,"school/home.html",{'students':student_data})


