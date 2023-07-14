from django.shortcuts import render
from .models import Customer,Products,Order

# Create your views here.

def getcustomers(request):
    get = Customer.objects.all()
    context = {"customer":get}
    return render(request,"customer.html",context)


def getproducts(request):
    product = Products.objects.select_related('customer')
    data = {"product":product}
    return render(request,'product.html',data)

def getorder(request):
    order = Order.objects.prefetch_related('customer')
    data = {'order':order}
    return render (request,"order.html",data)