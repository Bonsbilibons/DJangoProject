from asyncio.windows_events import NULL
from math import fabs
from re import X
from telnetlib import AUTHENTICATION
from unicodedata import category
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render , redirect
from django.core.files.storage import default_storage
from test_app.forms import UserCreationForm
from django.views import View
from django.contrib.auth import login
from django.contrib.auth import authenticate
import datetime
from .models import Categories, Payments, Products, Purchase_products, Purchases , Reviews , User 
from .servises.stripe import Stripe
from test_app.functions.functions import handle_uploaded_file
import uuid
import json
from django.core.mail import send_mail

from .servises.GoodsService import GoodsService
from .servises.CategoryService import CategoryService
from .servises.ReviewsService import ReviewsService
from .DTO.products.CreateProductDTO import CreateProductDTO
from .DTO.products.UpdateProductDTO import UpdateProductDTO
from .DTO.products.LeaveCommentDTO import LeaveCommentDTO



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



def show_goods(request , id):
    goods_service = GoodsService()
    category_service = CategoryService()
    if id == NULL :
        products = goods_service.get_all()
    else:
        products = goods_service.get_goods_by_category_id(id)
    return render(request, 'test_app/filter.html', {'products': products, 'categories': category_service.get_all(), 'id' : id })


def create_product(request):
    categories = CategoryService()
    return render(request, 'test_app/create.html', {'categories' : categories.get_all()} )

def create(request):
    goods_service = GoodsService()
    category = CategoryService()
    create_product_dto = CreateProductDTO(
        request.POST['name'], 
        request.POST['description'],
        request.POST['status'],
        request.POST['cost'],
        request.POST['amount'],
        request.FILES['icon'] if len(request.FILES) > 0 and request.FILES['icon'] else '',
        category.get_by_id(request.POST['category_id'])
    )
    goods_service.create_goods(create_product_dto)
    return redirect('/test_app/show/0')

def delete(request , id):
    if request.user.is_superuser :
        product = GoodsService()
        product.delete_by_id(id)
        return redirect('/test_app/show/0')

def edit(request , id):
    if request.user.is_superuser :
        product = GoodsService()
        return render(request, 'test_app/edit.html', {'object' : product.get_by_id(id) } )

def update(request):
    if request.user.is_superuser :
        goods_service = GoodsService()
        category = CategoryService()
        update_product_dto = UpdateProductDTO(
            request.POST['name'], 
            request.POST['description'],
            request.POST['status'],
            request.POST['cost'],
            request.POST['amount'],
            request.FILES['icon'] if len(request.FILES) > 0 and request.FILES['icon'] else '',
            category.get_by_id(request.POST['category_id'])
        )
        goods_service.update_goods(request.POST['id'], update_product_dto)
        return redirect('/test_app/show/0')

def detail(request , id):
    product = GoodsService()
    reviews = ReviewsService()
    return render(request, 'test_app/datail.html', {'object': product.get_by_id(id)  , 'reviews': reviews.filter_by_product_id(id)})

def leave_comment(request , id ):
    product = GoodsService()
    review = ReviewsService()
    leave_comment_dto = LeaveCommentDTO(
        request.user,
        request.POST['title'],
        request.POST['comment'],
        product.get_by_id(id)
    )
    review.leave_comment(leave_comment_dto)
    return redirect('/test_app/show/detail/' + str(id))

def delete_comment(request , id):
    review = ReviewsService()
    review.delete_by_id(request.POST['review_id'])
    return redirect('/test_app/show/detail/' + str(id))

class Register(View):
    template_name = 'registration/register.html'
    def get(self , request):
        context = {
             'form' : UserCreationForm()
             }
        return render(request , self.template_name , context)

    def post(self , request ):
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username , password = password)
            login(request , user)
        return redirect('/test_app/show/0')

def admin_panel(request):
    if request.user.is_superuser :

        products = Products.objects.all()
        json_prod = []

        reviews = Reviews.objects.all()

        for product in products:
            counter = 0 
            for review in reviews:
                if review.product.id == product.id:
                    counter += 1
            json_obj = {
                'id': product.id, 
                'name': product.name,
                'description': product.description,
                'cost': product.cost,
                'status': product.status,
                'amount' : product.amount,
                'category_name' : product.category.name ,
                'category_id' : product.category.id,
                'count_of_comments' : counter ,
            }
            json_prod.append(json_obj)
        return render(request , 'test_app/admin-panel.html' , {'products' : json_prod })


def cart(request):
    item = Products.objects.get(id = request.POST['id'])

    purchase = Purchases()
    purchase.purch_id = str(uuid.uuid4())
    if request.user.is_authenticated:
        purchase.user = request.user
    else :
        purchase.user = request.user.id
    purchase.total_sum = (item.cost * int(request.POST['amount']))
    purchase.status = '1'
    purchase.created_at = str(datetime.datetime.now()).split('.')[0]
    purchase.updated_at = str(datetime.datetime.now()).split('.')[0]
    purchase.save()

    product = Purchase_products()
    product.purchase = purchase
    product.product = item
    product.amount = request.POST['amount']
    product.created_at = str(datetime.datetime.now()).split('.')[0]
    product.updated_at = str(datetime.datetime.now()).split('.')[0]
    product.save()

    return render(request , 'test_app/checkout.html' , {'purchase' : purchase , 'product' : product})

def checkout(request):
    purchase = Purchases.objects.get(purch_id = request.POST['purch_id'])
    purchase.status = '2'
    purchase.updated_at = str(datetime.datetime.now()).split('.')[0]
    purchase.save()

    return render(request , 'test_app/payments_datail.html' , {'purchase' : purchase })

def stripe(request):
    purch_id = request.POST['purch_id']
    purchase = Purchases.objects.get(purch_id = purch_id)
    stripe = Stripe()
    stripe.add_card(request.POST['number'], request.POST['month'], request.POST['year'], request.POST['code'] )
    stripe.create_payment(request.POST['purchase'])
    purchase.payment_id = stripe.create_payment(request.POST['purchase'])
    purchase.save()
    payment = Payments()
    payment.card = request.POST['number']
    payment.email = request.POST['email']
    payment.created_at = str(datetime.datetime.now()).split('.')[0]
    payment.updated_at = str(datetime.datetime.now()).split('.')[0]
    payment.purchase = purchase
    payment.save()
    send_mail(
        'Confirm',
        f'Click on this url to submit the purchase  http://127.0.0.1:8000/test_app/confirm-payment/{purch_id}',
        'ivanbazelian@gmail.com',
        [request.POST['email']],
        fail_silently=False
        )
    return render(request , 'test_app/stripe.html' )

def confirm_payment(request , id):
     stripe = Stripe()
     purchase = Purchases.objects.get(purch_id = id)
     stripe.confirm_payment(purchase.payment_id)
     purchase.status = '3'
     purchase.updated_at = str(datetime.datetime.now()).split('.')[0]
     purchase.save()
     payment = Payments.objects.get(purchase_id = purchase.id)
     payment.updated_at = str(datetime.datetime.now()).split('.')[0]
     payment.save()
     return render(request , 'test_app/confirmed_payment.html' )

def orders(request):
    purchases = Purchases.objects.all()
    json_purchase = []
    for purchase in purchases:
        if purchase.user.id == request.user.id:
            purch_prod = Purchase_products.objects.get(id = purchase.id)
            json_purchase.append({
                'purch_id' : purchase.purch_id ,
                'total_sum' : purchase.total_sum,
                'created_at' : purchase.created_at,
                'amount' : purch_prod.amount,
                'product' : Products.objects.get(id = purch_prod.product.id)
            })
    return render(request , 'test_app/orders.html' , {'purchases' : json_purchase })