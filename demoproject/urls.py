"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import  settings
from  tender.views import (
    home_view,
    login_view,
    tender1_view,
    register_view,
    view_tender,
    admin_page_view,
    delete_item_view,
    loginadmin_view,
    find_min_bid_tender,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('login/',login_view,name='login'),
    path('loginadmin/',loginadmin_view,name='loginadmin'),
    path('register/',register_view,name='register'),
    path('tender_form/',view_tender,name='tender_form'),
    path('admin_page/',admin_page_view,name='admin_page'),
    path('find_min_bid_tender/',find_min_bid_tender,name='find_min_bid_tender'),
    path('delete_item/<int:item_id>',delete_item_view,name='delete_item'),
    
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
