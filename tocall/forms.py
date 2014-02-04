from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import History

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class HistoryCreateForm(ModelForm):

	class Meta:
		model = History
		fields = '__all__'
		widgets = {
			'write_up': Textarea(attrs={'cols': 30, 'rows': 5}),
		}

