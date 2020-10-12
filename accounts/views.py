from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm       #formularz standardowy django do wpisania użytkownika
    success_url = '/'   #reverse_lazy('SignUpView')       #żeby nie pisać z palca url to dajemy reverse_lazy i podajemy 'name' urla z urls.py
    template_name = 'login.html'   #wyświetlam formularz

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        login(self.request, self.object)
        return response