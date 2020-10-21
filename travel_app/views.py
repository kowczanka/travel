from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from django.views.generic.base import View

from travel_app.forms import CityModelForm, BlogModelForm, TravelModelForm, PlanModelForm, JournalModelForm
from travel_app.models import City, Blog, Travel, Plan, Travel_Journal


def index(request):
    user = request.user
    if user.is_superuser:
        return render(request, 'accounts/baseSuperuser.html')
    return render(request, 'base.html')

# CITY  ###################################################################################

class CityCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CityModelForm()
        return render(request, 'form.html', {'form': form, 'button_name': 'Add city'})

    def post(self, request):
        form = CityModelForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.author = request.user
            city.save()
            return redirect(reverse_lazy('CityView'))


class CityView(LoginRequiredMixin, View):
    def get(self, request):
        cities = City.objects.filter(author=request.user)
        if cities.count() == 0:
            return render(request, 'error.html', {'error_notice': 'You have nothing to display yet!', 'objects':cities})
        return render(request, 'ListView.html', {'objects': cities})


class UpdateCityView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        if id is None:
            form = CityModelForm()
        else:
            city = City.objects.get(pk=id)
            form = CityModelForm(instance=city)
        return render(request, 'form.html', {'form': form, 'button_name': 'Update city info'})

    def post(self, request, id=None):
        if id is None:
            form = CityModelForm(request.POST)
        else:
            city = City.objects.get(pk=id)
            form = CityModelForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('CityView'))


class DeleteCityView(LoginRequiredMixin, DeleteView):
    model = City
    fields = '__all__'
    template_name = 'delete.html'
    success_url = (reverse_lazy('CityView'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'button_name': "Delete"})
        return context

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


#   BLOG    ####################################################################################################################

class BlogCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = BlogModelForm()
        return render(request, 'form.html', {'form': form, 'button_name': 'Add post'})

    def post(self, request):
        form = BlogModelForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect(reverse_lazy('BlogView'))


class BlogView(View):
    def get(self, request):
        """wyświetla cały blog"""
        blogs = Blog.objects.all()
        return render(request, 'blog.html', {'objects': blogs})

def SeeBlog(request, id):
    """wyświetla pojedyncze posty"""
    post = Blog.objects.get(id=id)
    return render(request, 'SeeBlog.html', {'post': post})


class UpdateBlogView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        if id is None:
            form = BlogModelForm()
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogModelForm(instance=blog)
        return render(request, 'form.html', {'form': form, 'button_name': 'Update post info'})

    def post(self, request, id=None):
        if id is None:
            form = BlogModelForm(request.POST)
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogModelForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('BlogView'))


class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = Blog
    fields = '__all__'
    template_name = 'delete.html'
    success_url = (reverse_lazy('BlogView'))

    # def post(self, request, *args, **kwargs):
    #     blog = Blog.objects.get(pk=id)
    #     if blog.author == request.user:
    #         if request.POST['action'] == 'Cancel':
    #             self.object = self.get_object()
    #             success_url = self.get_success_url()
    #             return redirect(success_url)
    #         return self.delete(request, *args, **kwargs)
    #     return render(request, 'error.html', {'error_notice': "You can't delete posts of other authors"})


#   PLAN ####################################################################################################################

class PlanCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PlanModelForm()
        return render(request, 'form.html', {'form': form, 'button_name': 'Add plan'})

    def post(self, request):
        form = PlanModelForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)  # nie zapisze bloga do bazy danych, tylko stworzy obiekt Blog
            plan.author = request.user
            form.save()
            return redirect(reverse_lazy('PlanView'))


class PlanView(LoginRequiredMixin, View):
    def get(self, request):
        plans = Plan.objects.filter(author=request.user)
        if plans.count() == 0:
            return render(request, 'error.html', {'error_notice': "You have no plans yet"})
        return render(request, 'ListView.html', {'objects': plans})


class UpdatePlanView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        if id is None:
            form = PlanModelForm()
        else:
            plan = Plan.objects.get(pk=id)
            form = PlanModelForm(instance=plan)
        return render(request, 'form.html', {'form': form, 'button_name': 'Update travel plan'})

    def post(self, request, id=None):
        if id is None:
            form = PlanModelForm(request.POST)
        else:
            plan = Plan.objects.get(pk=id)
            form = PlanModelForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('PlanView'))


class DeletePlanView(LoginRequiredMixin, DeleteView):
    model = Plan

    fields = '__all__'
    template_name = 'delete.html'
    success_url = (reverse_lazy('PlanView'))

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


#   TRAVEL  ####################################################################################################################

class TravelCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TravelModelForm(logged_user=request.user)
        return render(request, 'form.html', {'form': form, 'button_name': 'Add travel'})

    def post(self, request):
        form = TravelModelForm(request.POST, logged_user=request.user)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.organizer = request.user
            form.save()
            return redirect(reverse_lazy('TravelView'))
        return render(request, 'form.html', {'form': form, 'button_name': 'Add travel'})


class TravelView(LoginRequiredMixin, View):
    def get(self, request):
        travels = Travel.objects.filter(organizer=request.user)
        if travels.count() == 0:
            return render(request, 'error.html', {'error_notice': "You have no travels yet"})
        return render(request, 'ListView.html', {'objects': travels})


class UpdateTravelView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        if id is None:
            form = TravelModelForm()
        else:
            travel = Travel.objects.get(pk=id)
            form = TravelModelForm(instance=travel)
        return render(request, 'form.html', {'form': form, 'button_name': 'Update travel info'})

    def post(self, request, id=None):
        if id is None:
            form = TravelModelForm(request.POST)
        else:
            travel = Travel.objects.get(pk=id)
            form = TravelModelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('TravelView'))


class DeleteTravelView(LoginRequiredMixin, DeleteView):
    model = Travel

    fields = '__all__'
    template_name = 'delete.html'
    success_url = (reverse_lazy('TravelView'))

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


#   JOURNAL ####################################################################################################################

class JournalCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = JournalModelForm(logged_user=request.user)
        return render(request, 'form.html', {'form': form, 'button_name': 'Add journal'})

    def post(self, request):
        form = JournalModelForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)  # nie zapisze bloga do bazy danych, tylko stworzy obiekt Blog
            journal.author = request.user
            form.save()
            return redirect(reverse_lazy('JournalView'))
        return render(request, 'form.html', {'form': form, 'button_name': 'Add journal'})


class JournalView(LoginRequiredMixin, View):
    def get(self, request):
        journals = Travel_Journal.objects.filter(author=request.user)
        if journals.count() == 0:
            return render(request, 'error.html', {'error_notice': "You have no journals yet"})
        return render(request, 'ListView.html', {'objects': journals})


class UpdateJournalView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        if id is None:
            form = JournalModelForm()
        else:
            journal = Travel_Journal.objects.get(pk=id)
            form = JournalModelForm(instance=journal)
        return render(request, 'form.html', {'form': form, 'button_name': 'Update travel info'})

    def post(self, request, id=None):
        if id is None:
            form = JournalModelForm(request.POST)
        else:
            journal = Travel_Journal.objects.get(pk=id)
            form = JournalModelForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('JournalView'))


class DeleteJournalView(LoginRequiredMixin, DeleteView):
    model = Travel_Journal

    fields = '__all__'
    template_name = 'delete.html'
    success_url = (reverse_lazy('JournalView'))

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'Cancel':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)
