from django import forms

# from accounts.models import Account
from django.contrib.auth.models import User

from travel_app.models import City, Blog, Travel, Plan, Travel_Journal


class CityModelForm(forms.ModelForm):

    class Meta:
        model = City
        fields = "__all__"

class BlogModelForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ("author",)
        widgets = {
            'date_of_creation': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control','type': 'date'}),
        }

class TravelModelForm(forms.ModelForm):

    class Meta:
        model = Travel
        fields = "__all__"
        widgets = {
            'country':forms.Select(),
            'end_date': forms.DateInput(format=('%m-%d-%Y'),
                                             attrs={'firstDay': 1, 'format': 'yyyy-mm-dd', 'type': 'date'}),
            'start_date': forms.DateInput(format=('%m-%d-%Y'),
                                        attrs={'firstDay': 1, 'format': 'yyyy-mm-dd', 'type': 'date'})
        }

class PlanModelForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = "__all__"



class JournalModelForm(forms.ModelForm):

    class Meta:
        model = Travel_Journal
        fields = "__all__"