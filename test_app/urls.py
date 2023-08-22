from xml.etree.ElementInclude import include
from django.urls import path , include

from . import views

from django.conf import settings
from django.conf.urls.static import static

from test_app.views import Register




urlpatterns = [
    path('products/', views.products, name='products'),
    path('create-product/', views.create_product, name='creation'),
    path('create-product/create', views.create, name='create'),
    path('show/', views.show_goods, name='show'),
    path('show/<int:id>', views.show_goods, name='show'),
    path('show/detail/<int:id>', views.detail, name='detail'),
    path('show/detail/<int:id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update', views.update, name='update'),
    path('account/' , include('django.contrib.auth.urls')),
    path('register/' , Register.as_view() , name = 'register'),
    path('admin-panel/' , views.admin_panel , name = 'admin-panel'),
    path('cart/' , views.cart , name = 'cart') ,
    path('checkout/', views.checkout , name = 'checkout'),
    path('stripe/', views.stripe , name = 'stripe'),
    path('confirm-payment/<id>' , views.confirm_payment , name = 'confirm_payment'),
    path('orders/' , views.orders , name = 'orders'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)