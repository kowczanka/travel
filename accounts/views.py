from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import User, Permission




# class SignUpView(CreateView):
#     ''' widok rejestracji użytkowanika'''
#     form_class = UserCreationForm
#     success_url = '/'
#     template_name = 'login.html'
#
#     def form_valid(self, form):
#         response = super(SignUpView, self).form_valid(form)
#         login(self.request, self.object)
#         return response
from accounts.forms import AbstractUserForm


class myLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'button_name': 'login, gurl!'})
        return context

class SignUpView(CreateView):
    form_class = AbstractUserForm
    success_url = reverse_lazy('home')
    template_name = 'form.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        login(self.request, self.object)

        user = self.object
        # permissions = Permission.objects.filter(codename__icontains='movie')
        # user.user_permissions.add(Permission.objects.get(codename='add_movie'))
        # user.user_permissions.add(permissions.get(codename='delete_movie'))
        login(self.request, self.object)

        return response

class CreateUser(View):
    def get(self, request):
        form = AbstractUserForm()
        context = {"form":form, 'button_name':"register, gurl"}
        return render (request, 'form.html', context)

    def post(self,request):
        form = AbstractUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("home"))
        return HttpResponse("Invalid form")

class UserListView(ListView):
    model=User
    template_name = 'ListView.html'

    def get_queryser(self):
        return User.objects.filter(is_superuser=False)
