from django.contrib import admin
from .models import Customer,Bookmark,CustomerBookmark

# Register your models here.
admin.site.register(Customer)
admin.site.register(Bookmark)
admin.site.register(CustomerBookmark)
