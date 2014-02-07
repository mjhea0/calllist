from django import forms
from django.forms import ModelForm, Textarea, DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets                                       
from django.shortcuts import get_object_or_404

from .models import History, Contact

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class HistoryCreateForm(ModelForm):

	class Meta:
		model = History
		fields = '__all__'
		widgets = {
			'write_up': Textarea(attrs={'cols': 50, 'rows': 3}),
		}

class ContactNextCallForm(ModelForm):
    class Meta:
		model = Contact
		fields = ['next_call']

    def __init__(self, *args, **kwargs):
        super(ContactNextCallForm, self).__init__(*args, **kwargs)
        self.fields['next_call'].widget = widgets.AdminDateWidget()
        # self.fields['mytime'].widget = widgets.AdminTimeWidget()
        # self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()
