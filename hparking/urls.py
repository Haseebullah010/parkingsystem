"""hparking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from parking import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('mainpage/', views.signin, name='SIGNIN'),
    path('flat/', views.flats, name='FLAT'),
    path('slot/', views.slots, name='SLOT'),
    path('check_pourchnum/', views.check_pourchnum, name='check_pourchnum'),
    path('delete_product/', views.delete_product, name='DELETE_PRODUCT'),
    path('all2/', views.delete_item, name='DELETE'),
    path('all/', views.all, name='ALL'),
    path('user_logout/',views.user_logout,name="USER_LOGOUT"),
    path('main/',views.add,name="addition"),


    path('admin/', admin.site.urls),


]
