from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm  # pick one depending if you want old pwd check
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class SignupForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):

            fields = ('username', 'first_name', 'last_name', 'email',)



class UserUpdateForm(PasswordChangeForm, forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        if 'email' in self.changed_data and 'new_password1' in self.changed_data:
            raise ValidationError("Don't change password and email at same time!")


    def __init__(self, *args, **kwargs):
        super().__init__(user=kwargs.get('instance'), *args, **kwargs)
        self.fields['new_password1'].required = False
        self.fields['new_password2'].required = False
        
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            password_validation.validate_password(password2, self.user)
        elif password1 or password2:
            raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2
    def save(self, commit=True):
        password = self.cleaned_data.get("new_password1")
        if password:
             self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user