# bookmark-manager

Bookmark Manager

software saves and organizes web content and websites so users can refer to it later.
Bookmark managers will either work alongside, or inside of, a web browser, allowing users to save web content and return to it later without opening another application.

<h1>Django Filter</h1>

Django-filter is a reusable Django application allowing users to declaratively add dynamic QuerySet filtering from URL parameters.

Full documentation on read the docs.

https://dev.azure.com/noumenal/Django%20Filter/_apis/build/status/Django%20Filter-CI https://travis-ci.org/carltongibson/django-filter.svg?branch=master  

<h1>Requirements</h1>

Python: 3.5, 3.6, 3.7, 3.8

Django: 2.2, 3.0

DRF: 3.10+

From Version 2.0 Django Filter is Python 3 only. If you need to support Python 2.7 use the version 1.1 release.

<h1>Installation</h1>

Install using pip:

pip install django-filter

Then add 'django_filters' to your INSTALLED_APPS.

INSTALLED_APPS = 

[
    ...
    'django_filters',
    
]

<h1>Usage</h1>

Django-filter can be used for generating interfaces similar to the Django admin's list_filter interface. It has an API very similar to Django's ModelForms. For example, if you had a Product model you could have a filterset for it with the code:

import django_filters

<h1>Integration with DRF</h1>

Integration with Django Rest Framework is provided through a DRF-specific FilterSet and a filter backend. These may be found in the rest_framework sub-package.

Using the new FilterSet simply requires changing the import path. Instead of importing from django_filters, import from the rest_framework sub-package.


from django_filters import rest_framework as filters


Your view class will also need to add DjangoFilterBackend to the filter_backends.



from django_filters import rest_framework as filters

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

If you want to use the django-filter backend by default, add it to the DEFAULT_FILTER_BACKENDS setting.

# settings.py

INSTALLED_APPS = 

[
    ...
    
    'rest_framework',
    
    'django_filters',
    
]

REST_FRAMEWORK =
{
    
    'DEFAULT_FILTER_BACKENDS': (
    
        'django_filters.rest_framework.DjangoFilterBackend',
        
        ...
    ),
}

<h1>Generic Filtering</h1>

As well as being able to override the default queryset, REST framework also includes support for generic filtering backends that allow you to easily construct complex searches and filters.

Generic filters can also present themselves as HTML controls in the browsable API and admin API.



![alt text](https://www.django-rest-framework.org/img/filter-controls.png)



<h3>Setting filter backends</h3>

The default filter backends may be set globally, using the DEFAULT_FILTER_BACKENDS setting. For example.

REST_FRAMEWORK = 

{

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
    
}

You can also set the filter backends on a per-view, or per-viewset basis, using the GenericAPIView class-based views.

import django_filters.rest_framework

from django.contrib.auth.models import User

from myapp.serializers import UserSerializer

from rest_framework import generics

class UserListView(generics.ListAPIView):

    queryset = CustomerBookmark.objects.all()
    
    serializer_class = CustomerBookmarkSerializer
    
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]



<h1>DjangoFilterBackend</h1>

The django-filter library includes a DjangoFilterBackend class which supports highly customizable field filtering for REST framework.

To use DjangoFilterBackend, first install django-filter. Then add django_filters to Django's INSTALLED_APPS

pip install django-filter

You should now either add the filter backend to your settings:

REST_FRAMEWORK =

{

'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']

}

Or add the filter backend to an individual View or ViewSet.

from django_filters.rest_framework import DjangoFilterBackend

class UserListView(generics.ListAPIView):

    ...
    
    filter_backends = [DjangoFilterBackend]
    
If all you need is simple equality-based filtering, you can set a filterset_fields attribute on the view, or viewset, listing the set of fields you wish to filter against.

class CustBookMarkList(generics.ListAPIView):

    queryset = CustomerBookmark.objects.all()
    
    serializer_class = CustomerBookmarkSerializer
    
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    
<h1>SearchFilter</h1>

The SearchFilter class supports simple single query parameter based searching, and is based on the Django admin's search functionality.

When in use, the browsable API will include a SearchFilter control:

The SearchFilter class will only be applied if the view has a search_fields attribute set. The search_fields attribute should be a list of names of text type fields on the model, such as CharField or TextField.

from rest_framework import filters


class CustBookMarkList(generics.ListAPIView):

    queryset = CustomerBookmark.objects.all()
    
    serializer_class = CustomerBookmarkSerializer
    
    filter_backends = (DjangoFilterBackend,OrderingFilter)


<h1>OrderingFilter</h1>


The OrderingFilter class supports simple query parameter controlled ordering of results.


















