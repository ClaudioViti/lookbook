from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm  # pick one depending if you want old pwd check
from django.contrib.auth.models import User




class SignupForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):

            fields = ('username', 'first_name', 'last_name', 'email',)



class UserUpdateForm(PasswordChangeForm, forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(user=kwargs.get('instance'), *args, **kwargs)