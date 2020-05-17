# from django.db import models
from django.db import models
from django_extensions.db.models import TimeStampedModel
from model_utils.models import TimeFramedModel

# Create your models here.
class Customer(TimeStampedModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField( max_length=255, blank=True,null=True)
    email = models.EmailField(max_length=255,blank=True,null=True)
    lat = models.DecimalField(max_digits =10,decimal_places =3)
    lng = models.DecimalField(max_digits =10,decimal_places =3)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name

class Bookmark(TimeStampedModel):
    title = models.CharField(max_length=255) 
    url = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmarks"

    def __str__(self):
        return self.title

class CustomerBookmark(TimeStampedModel,TimeFramedModel):
    customer = models.ForeignKey(Customer, related_name="+", blank=True, null=True,  on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Bookmark, related_name="+", blank=True, null=True,  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CustomerBookmark"
        verbose_name_plural = "CustomerBookmarks"
