from django.contrib import admin

from .models import Products
from .models import User
from .models import Reviews
from .models import Categories

admin.site.register(Products)
admin.site.register(User)
admin.site.register(Reviews)
admin.site.register(Categories)