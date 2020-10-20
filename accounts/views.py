from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import User, Permission, Group

from accounts.forms import UserForm, PermissionForm, PermissionFormGroup


class myLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'button_name': 'login!'})
        return context

class SignUpView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'form.html'
    initial = {"is_traveler": False}

    def clean_email(self):
        form = UserForm
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        login(self.request, self.object)
        grupa, created = Group.objects.get_or_create(name='travelers')
        user = self.object
        if form.cleaned_data.get('is_traveler'):
            user.groups.add(grupa)

        permissions = Permission.objects.filter(content_type_id__in = [7,8,9,10])
        user.user_permissions.set(permissions) #set bo to lista QuerySet
        login(self.request, self.object)
        return response


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'accounts/permissionsList.html', {'objects': users})

    def test_func(self):
        return self.request.user.is_superuser


class ChangePermissionView(UserPassesTestMixin, UpdateView):
    form_class = PermissionForm
    success_url = '/'
    model = User
    template_name = 'form.html'

    def test_func(self):
        return self.request.user.is_superuser

class GroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'accounts/permissionsList.html', {'objects': groups})

    def test_func(self):
        return self.request.user.is_superuser

class ChangePermissionViewGroup(UserPassesTestMixin, UpdateView):
    form_class = PermissionFormGroup
    success_url = '/'
    model = Group
    template_name = 'form.html'

    def test_func(self):
        return self.request.user.is_superuser


    #ta funkcja zwraca travelers_group - czy moze tak być? czy nie musi nic zwracać


    def traveler_group_permissions(self):
        travelers_group = Group.objects.get(name='travelers')
        travelers_perm = Permission.objects.filter(content_type_id__in=[10, 11])
        travelers_group.permissions.set(travelers_perm)
        return travelers_group

class UserList(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'accounts/UserList.html', {'objects': users})

    def test_func(self):
        return self.request.user.is_superuser

def user_details(request, id):
    user_to_see = User.objects.get(id=id)
    return render(request, 'accounts/UserDetails.html', {'objects': user_to_see})


def delete_user(request, id):
        user_to_delete = User.objects.get(id = id)
        user_to_delete.delete()
        return render (request, 'error.html', {'error_notice': "User deleted"})

