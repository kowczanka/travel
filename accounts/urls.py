from django.contrib import admin
from django.urls import path, include
from accounts.views import myLoginView, SignUpView, UserView, ChangePermissionView, \
    ChangePermissionViewGroup, GroupView, delete_user, UserList, user_details  # CreateUser
# UserListView,
urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('SignUpView/', SignUpView.as_view(), name='SignUpView'),

    path('myLoginView/', myLoginView.as_view(), name='myLoginView'),
   # path('CreateUser/', CreateUser.as_view(), name='CreateUser'),

    # path('UserListView/', UserListView.as_view(), name='UserListView'),

    path('ChangePermissionView/<int:pk>', ChangePermissionView.as_view(), name='ChangePermissionView'),
    path('ChangePermissionViewGroup/<int:pk>', ChangePermissionViewGroup.as_view(), name='ChangePermissionViewGroup'),

    path('UserView/', UserView.as_view(), name='UserView'),
    path('GroupView/', GroupView.as_view(), name='GroupView'),

    path('UserList/', UserList.as_view(), name='UserList'),
    path('user_details/<int:id>', user_details, name='user_details'),

    path('delete_user/<int:id>', delete_user, name='delete_user'),

]
