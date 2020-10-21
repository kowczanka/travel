from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):

    email = forms.EmailField(required=True)
    is_traveler = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_traveler')



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