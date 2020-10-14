"""travel_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from travel_app.views import index, CityCreateView, CityView, UpdateCityView, DeleteCityView, DeleteBlogView, \
    DeleteTravelView
from travel_app.views import  BlogCreateView, BlogView, UpdateBlogView, \
    UpdateTravelView, TravelView, TravelCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "home"),
    path('accounts/', include('accounts.urls')),

    path('CityCreateView/', CityCreateView.as_view(), name='CityCreateView'),
    path('CityView/', CityView.as_view(), name='CityView'),
    path('UpdateCityView/<int:id>/', UpdateCityView.as_view(), name='UpdateCityView'),
    path('DeleteCityView/<int:pk>/', DeleteCityView.as_view(), name='DeleteCityView'),



    path('BlogCreateView/', BlogCreateView.as_view(), name='BlogCreateView'),
    path('BlogView/', BlogView.as_view(), name='BlogView'),
    path('UpdateBlogView/<int:id>/', UpdateBlogView.as_view(), name='UpdateBlogView'),
    path('DeleteBlogView/<int:pk>/', DeleteBlogView.as_view(), name='DeleteBlogView'),

    path('TravelCreateView/', TravelCreateView.as_view(), name='TravelCreateView'),
    path('TravelView/', TravelView.as_view(), name='TravelView'),
    path('UpdateTravelView/<int:id>/', UpdateTravelView.as_view(), name='UpdateTravelView'),
    path('DeleteTravelView/<int:pk>/', DeleteTravelView.as_view(), name='DeleteTravelView'),


]
