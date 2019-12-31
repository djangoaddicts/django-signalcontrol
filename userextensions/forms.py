from django import forms

# import models
from userextensions.models import (UserPreference)


class UserPreferenceForm(forms.ModelForm):
    """ Form class used to add/edit UserPreference objects """
    class Meta:
        model = UserPreference
        exclude = ['created_at', 'updated_at', 'user']
        widgets = {
            'recents_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'page_refresh_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'start_page': forms.TextInput(attrs={'class': 'form-control'}),
        }
