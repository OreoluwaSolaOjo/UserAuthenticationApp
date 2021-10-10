from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    password = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'type': 'hidden', }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    # to style add widget since we want to change the default django style
    first_name = forms.CharField(
        max_length=100, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(
        max_length=100, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
    # to style the remainig fields password1 and password2 and username

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. </small></span>'
        self.fields['username'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class= "form-text text-muted"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class= "form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
