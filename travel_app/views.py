
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from django.views.generic.base import View

from travel_app.forms import CityModelForm, BlogModelForm, TravelModelForm
from travel_app.models import City, Blog, Travel


def index(request):
    return render(request, 'base.html')

class CityCreateView(View):
    def get(self, request):
        form = CityModelForm()
        return render(request, 'form.html', {'form':form, 'button_name':'Add city'})

    def post(self, request):
        form = CityModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('CityView'))


class CityView(View):
    def get(self, request):
        cities = City.objects.all()
        return render(request, 'ListView.html', {'objects': cities})

class UpdateCityView(View):
    def get(self, request, id=None):
        if id is None:
            form = CityModelForm()
        else:
            city = City.objects.get(pk=id)
            form = CityModelForm(instance=city)
        return render(request, 'form.html', {'form': form, 'button_name':'Update city info'})

    def post(self, request, id=None):
        if id is None:
            form = CityModelForm(request.POST)
        else:
            city = City.objects.get(pk=id)
            form = CityModelForm(request.POST,
                                  instance=city)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('CityView'))

class DeleteCityView(DeleteView):
    model = City
    fields = '__all__'
    template_name = 'delete.html'
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'button_name' : "Delete"})
        return context

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)

class BlogCreateView(View):
    def get(self, request):
        form = BlogModelForm()
        return render(request, 'form.html', {'form':form, 'button_name':'Add post'})

    def post(self, request):
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('BlogView'))


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog.html', {'objects': blogs})

class UpdateBlogView(View):
    def get(self, request, id=None):
        if id is None:
            form = BlogModelForm()
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogModelForm(instance=blog)
        return render(request, 'form.html', {'form': form, 'button_name':'Update post info'})

    def post(self, request, id=None):
        if id is None:
            form = BlogModelForm(request.POST)
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogModelForm(request.POST,
                                  instance=blog)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('BlogView'))

class DeleteBlogView(DeleteView):
    model = Blog

    fields = '__all__'
    template_name = 'delete.html'
    success_url = ''

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


class TravelCreateView(View):
    def get(self, request):
        form = TravelModelForm()
        return render(request, 'form.html', {'form':form, 'button_name':'Add travel'})

    def post(self, request):
        form = TravelModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('TravelView'))


class TravelView(View):
    def get(self, request):
        travels = Travel.objects.all()
        if travels.count() > 0:
            return render(request, 'blog.html', {'objects': travels})
        return render(request, 'error.html')

class UpdateTravelView(View):
    def get(self, request, id=None):
        if id is None:
            form = TravelModelForm()
        else:
            travel = Travel.objects.get(pk=id)
            form = TravelModelForm(instance=travel)
        return render(request, 'form.html', {'form': form, 'button_name':'Update travel info'})

    def post(self, request, id=None):
        if id is None:
            form = TravelModelForm(request.POST)
        else:
            travel = Travel.objects.get(pk=id)
            form = TravelModelForm(request.POST,
                                  instance=travel)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('TravelView'))


class DeleteTravelView(DeleteView):
    model = Travel

    fields = '__all__'
    template_name = 'delete.html'
    success_url = ''

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)