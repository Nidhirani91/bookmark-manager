from django.urls import path
# from django.contrib import admin
from django.conf.urls import url
  
# from employee import views  

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('admin/', admin.site.urls),  
    # path('cust', views.cust,name='cust'),  
    # path('show',views.show,name='show'),  
    # path('edit/<int:id>', views.edit,name='edit'),  
    # path('update/<int:id>', views.update),  
    # path('delete/<int:id>', views.delete,name='delete'),
    
    path('cust_list/', views.customer_list),
    path('cust_list/<int:pk>/', views.customer_detail),
    path('book_list/', views.bookmark_list),
    path('book_list/<int:pk>/', views.bookmark_detail),
    path('custbookmark_list/', views.CustBookMarkList.as_view(),name='custbookmark_list'),
    path('custbookmark_list/add/', views.custbookmark_add),
    path('custbookmark_list/<int:pk>/', views.custbookmark_detail),

    # path('bookmarkcreate', views.bookmarkcreate,name='bookmarkcreate'),  
    # path('bookmarkshow',views.bookmarkshow,name='bookmark_show'),  
    # path('bookmarkedit/<int:id>', views.bookmarkedit,name='bookmark_edit'),  
    # path('bookmarkupdate/<int:id>', views.bookmarkupdate),  
    # path('bookmarkdelete/<int:id>', views.bookmarkdelete,name='bookmarkdelete'),
]
