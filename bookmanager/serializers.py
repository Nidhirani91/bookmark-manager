from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets,generics
from django.utils.text import slugify

from . import models


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model =models.Customer
		fields = ['id','name', 'address', 'phone', 'email','lat','lng',]

class BookmarkSerializer(serializers.ModelSerializer):
	class Meta:
		model =models.Bookmark
		fields = ['id','title','url', 'source_name']

class CustomerBookmarkSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer()
	bookmark = BookmarkSerializer()
	class Meta:
		model =models.CustomerBookmark
		fields = ['id','start','end','customer', 'bookmark']


class CustomerBookmarkAddSerializer(serializers.ModelSerializer):
	class Meta:
		model =models.CustomerBookmark
		fields = ['id','start','end','customer', 'bookmark']



