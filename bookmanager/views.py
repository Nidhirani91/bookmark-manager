from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework import permissions, status, viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# from django_filters import rest_framework as filters
from .models import Customer,Bookmark,CustomerBookmark
from .serializers import CustomerSerializer, BookmarkSerializer,CustomerBookmarkSerializer,CustomerBookmarkAddSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
# Create your views here 

@csrf_exempt
@api_view(['GET', 'POST'])
def customer_list(request):
	"""
	List all language.
	"""
	if request.method == 'GET':
		cust =Customer.objects.all()
		serializer = CustomerSerializer(cust, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = CustomerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
	"""
	Retrieve, update or delete languages.
	"""
	try:
		cust =Customer.objects.get(pk=pk)
	except Customer.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CustomerSerializer(cust)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CustomerSerializer(cust, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		cust.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
def bookmark_list(request):
	"""
	List all language.
	"""
	if request.method == 'GET':
		bookmarkcreate =Bookmark.objects.all()
		serializer = BookmarkSerializer(bookmarkcreate, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = BookmarkSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def bookmark_detail(request, pk):
	"""
	Retrieve, update or delete languages.
	"""
	try:
		bookmarkcreate =Bookmark.objects.get(pk=pk)
	except Bookmark.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BookmarkSerializer(bookmarkcreate)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = BookmarkSerializer(bookmarkcreate, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		bookmarkcreate.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class CustBookMarkList(generics.ListAPIView):
    queryset = CustomerBookmark.objects.all()
    serializer_class = CustomerBookmarkSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filter_fields ={
    'start':['date__range', ],
    'end':['date__range', ],
    'customer__id':['exact'],
    'customer__lat':['exact'],
    'customer__lng':['exact'],
    'bookmark__title':['exact'],
    'bookmark__source_name':['exact'],
   
}

@csrf_exempt
@api_view(['GET', 'POST'])
def custbookmark_add(request):
	
	if request.method == 'GET':
		bookmarkcreate =CustomerBookmark.objects.all()
		serializer = CustomerBookmarkAddSerializer(bookmarkcreate, many=True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		serializer = CustomerBookmarkAddSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def custbookmark_detail(request, pk):
	"""
	Retrieve, update or delete CustomerBookmark.
	"""
	try:
		custbookmark =CustomerBookmark.objects.get(pk=pk)
	except CustomerBookmark.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CustomerBookmarkSerializer(custbookmark)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CustomerBookmarkAddSerializer(custbookmark, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		custbookmark.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
