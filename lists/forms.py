from django import forms
from django.forms import ModelForm, TextInput
from .models import ListName, ListItem


class ListForm(ModelForm):
    class Meta:
        model = ListName
        fields = ['list_name']
        widgets = {
            'list_name': TextInput(attrs={
                'class': 'form-control mb-3',
                'style': 'max-width: 300px',
                'placeholder': 'New List Name'
            })
        }

class EditListForm(forms.Form):
    list_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'style': 'max-width: 300px'}))

class AddItemForm(ModelForm):
    class Meta:
        model = ListItem
        fields = ['list_item']
        widgets = {
            'list_item': TextInput(attrs={
                'class': 'form-control mb-3',
                'style': 'max-width: 300px',
                'placeholder': 'New Item'
            })
        }

class EditItemForm(forms.Form):
    list_item = forms.CharField(max_length=100)

