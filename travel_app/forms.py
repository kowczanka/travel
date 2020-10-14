from django import forms

from travel_app.models import City, Blog, Travel


class CityModelForm(forms.ModelForm):

    class Meta:
        model = City
        fields = "__all__"

class BlogModelForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = "__all__"
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
            'end_date': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl',
                                                    'format': 'yyyy-mm-dd', 'type': 'date'}),
            'start_date': forms.DateInput(format=('%d-%m-%Y'),
                                        attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl',
                                               'format': 'yyyy-mm-dd', 'type': 'date'})
        }

