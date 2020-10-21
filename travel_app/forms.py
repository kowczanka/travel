from django import forms

# from accounts.models import Account
from django.contrib.auth.models import User

from travel_app.models import City, Blog, Travel, Plan, Travel_Journal


class CityModelForm(forms.ModelForm):

    class Meta:
        model = City
        exclude = ("author",)
        fields = "__all__"

class BlogModelForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ("author",)
        widgets = {
            'date_of_creation': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control','type': 'date'}),
        }


class PlanModelForm(forms.ModelForm):

    # def __init__(self, *args,logged_user=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['travel'].queryset = Travel.objects.filter(organizer=logged_user)

    class Meta:
        model = Plan
        exclude = ("author",)
        fields = "__all__"


class TravelModelForm(forms.ModelForm):

    def __init__(self, *args,logged_user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trip_plan'].queryset = Plan.objects.filter(author_id=logged_user)

    class Meta:
        model = Travel
        exclude = ("organizer",)
        fields = "__all__"
        widgets = {
            'country':forms.Select(),
            'end_date': forms.DateInput(format=('%m-%d-%Y'),
                                             attrs={'firstDay': 1, 'format': 'yyyy-mm-dd', 'type': 'date'}),
            'start_date': forms.DateInput(format=('%m-%d-%Y'),
                                        attrs={'firstDay': 1, 'format': 'yyyy-mm-dd', 'type': 'date'})
        }

class JournalModelForm(forms.ModelForm):

    def __init__(self, *args,logged_user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['travel'].queryset = Travel.objects.filter(organizer=logged_user)

    class Meta:
        model = Travel_Journal
        exclude = ("author",)
        fields = "__all__"