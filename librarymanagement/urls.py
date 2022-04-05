"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from xmlrpc.client import Server
from urllib.parse import urlparse
from django.urls import resolve
from django.http import Http404, HttpResponseRedirect
from django.contrib import admin

from django.urls import include, re_path
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
#from django.conf.urls import  re_path
admin.site.site_header = "Library Management System Admin"
admin.site.site_title = "Library Management System Admin Portal"
admin.site.index_title = "Welcome to Library Management System"

# """

# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import *

# urlpatterns = [
# 	path('image_upload', hotel_image_view, name = 'image_upload'),
# 	path('success', success, name = 'success'),
# ]

# if settings.DEBUG:
# 		urlpatterns += static(settings.MEDIA_URL,
# 							document_root=settings.MEDIA_ROOT)

# """

urlpatterns = [
    #path('',include('Court.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
   # path('', views.index, name='index'),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('cart', views.cart_view),
    # path('removefromcart', views.removefromcart_view),
    path('viewbook', views.viewbook_view),
    path('getbooks', views.getbooks_view),
   
    path('displaybook', views.displaybook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent),


]

#if settings.DEBUG:
#        urlpatterns += static(settings.MEDIA_URL,
#                             document_root=settings.MEDIA_ROOT)

urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
