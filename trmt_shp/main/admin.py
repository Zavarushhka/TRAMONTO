from django.contrib import admin
from .models import Order, LikeBlock, Like

# Register your models here.

admin.site.register(LikeBlock)
admin.site.register(Like)
admin.site.register(Order)
