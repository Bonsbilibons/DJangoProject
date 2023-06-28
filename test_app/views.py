from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render , redirect
from django.core.files.storage import default_storage
from .models import Products
from .forms import UploadFileForm
import uuid
import json



def products(request):
    products = Products.objects.all()
    json_data = []
    for product in products:
        json_obj = {
            'id': product.id, 
            'name': product.name,
            'description': product.description,
            'cost': product.cost,
            'status': product.status,
            'amount' : product.amount,
        }
        json_data.append(json_obj)
    return HttpResponse(json.dumps(json_data), content_type="application/json")

def main(request):
    return render(request , 'test_app/main.html' )


def show_goods(request):
    product = Products.objects.all()
    products = Products.objects.all()
    json_data = []
    for product in products:
        json_obj = {
            'id': product.id, 
            'name': product.name,
            'description': product.description,
            'cost': product.cost,
            'status': product.status,
            'amount' : product.amount,
        }
        json_data.append(json_obj)
    return render(request , 'test_app/show.html' , { 'object' : json_data })


def create_product(request):
    return render(request , 'test_app/create.html'  )

def create(request):
    product = Products()
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.cost = request.POST['cost']
    product.status = request.POST['status']
    product.amount = request.POST['amount']
    if request.FILES['icon'] != '':
        product.icon = request.FILES['icon']
    product.save()
    return render(request ,'test_app/create.html'  )


def delete(request , id):
    Products.objects.get(id = id).delete()
    return redirect('/test_app/show/')




def edit(request , id):
    prod = Products.objects.get(id = id)
    return render(request , 'test_app/edit.html' , {'object' : prod } )


def update(request):
    product = Products.objects.get(id = request.POST['id'])
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.cost = request.POST['cost']
    product.status = request.POST['status']
    product.amount = request.POST['amount']
    if request.FILES['icon'] == '':
        product.icon = request.FILES['icon']
    product.save()
    return redirect('/test_app/show/')

def detail(request , id):
    prod = Products.objects.get(id = id)
    return render(request , 'test_app/datail.html' , {'object' : prod })

