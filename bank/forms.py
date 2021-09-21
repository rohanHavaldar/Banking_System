from django import forms
from .models import *

class ActionForm(forms.ModelForm):
    #username =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #email_id =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #contact =  forms.IntegerField(widget=forms.TextInput(attrs={'disabled':'True'}))
    class Meta:
        model = Action
        fields = ["username", "email_id", "contact", "amount"]

class TransactionForm(forms.ModelForm):
    #username =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #email_id =  forms.CharField(widget=forms.TextInput(attrs={'disabled':'True'}))
    #contact =  forms.IntegerField(widget=forms.TextInput(attrs={'disabled':'True'}))
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), initial=0)
    class Meta:
        model = Transact
        fields = ["username", "email_id", "contact", "amount","receiver"]