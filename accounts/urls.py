from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView, UserView, ChangePermissionView, \
    ChangePermissionViewGroup, GroupView, UserList, UserDetails, DeleteUser

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('SignUpView/', SignUpView.as_view(), name='SignUpView'),

    path('ChangePermissionView/<int:pk>', ChangePermissionView.as_view(), name='ChangePermissionView'),
    path('ChangePermissionViewGroup/<int:pk>', ChangePermissionViewGroup.as_view(), name='ChangePermissionViewGroup'),

    path('UserView/', UserView.as_view(), name='UserView'),
    path('GroupView/', GroupView.as_view(), name='GroupView'),
    path('UserList/', UserList.as_view(), name='UserList'),

    path('user_details/<int:id>', UserDetails.as_view(), name='user_details'),
    path('delete_user/<int:id>', DeleteUser.as_view(), name='delete_user'),

]
