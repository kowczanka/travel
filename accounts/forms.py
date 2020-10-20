from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm

# from accounts.models import Account
from django.contrib.auth.models import User, Group


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, label="Name*", required=False)
    last_name = forms.CharField(max_length=50, label="Surname*", required=False)
    is_traveler = forms.BooleanField(required=False)


class PermissionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_permissions',)
        labels = {
            'user_permissions': "User permissions"
        }
        widgets = {
            'user_permissions':forms.CheckboxSelectMultiple()
        }

class PermissionFormGroup(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('permissions',)
        labels = {
            'permissions': "Group permissions"
        }
        widgets = {
            'permissions':forms.CheckboxSelectMultiple()
        }