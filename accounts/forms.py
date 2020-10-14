from django import forms

from accounts.models import Account


class AbstractUserForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "is_traveler", "password")
        widgets = {
            'is_traveler':forms.Select()
        }