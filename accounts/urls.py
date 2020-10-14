from django.contrib import admin
from django.urls import path, include
from accounts.views import myLoginView, CreateUser, SignUpView, UserListView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('SignUpView/', SignUpView.as_view(), name='SignUpView'),

    path('myLoginView/', myLoginView.as_view(), name='myLoginView'),
    path('CreateUser/', CreateUser.as_view(), name='CreateUser'),

    path('UserListView/', UserListView.as_view(), name='UserListView'),







]
